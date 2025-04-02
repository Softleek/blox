import random
import string
import uuid

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from ..utils.get_model_details import get_model_doctype_json


def generate_random_slug(length=10):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


def generate_by_hash():
    """Generate a random hash-based name."""
    return str(uuid.uuid4())


class BaseModel(models.Model):
    id = models.CharField(
        primary_key=True, max_length=255, default=generate_by_hash, editable=True
    )
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who created this record.",
    )
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who last modified this record.",
    )

    class Meta:
        abstract = True


class SingletonModel(BaseModel):
    """
    Abstract base class for singleton models.
    Uses config name as ID (CharField) instead of AutoField.
    """
    id = models.CharField(
        primary_key=True,
        max_length=100,
        editable=False
    )

    # Track if instance was just created
    _just_created = False

    class Meta:
        abstract = True
        
    @classmethod
    def get(cls, *args, **kwargs):
        """Override the default get() to return the singleton instance"""
        if not kwargs and not args:  # If no filters provided
            return cls.get_instance()
        return super().get(*args, **kwargs) 

    def get_config_based_id(self):
        """Get the ID based on model's doctype config or fallback to model name"""
        try:
            doctype_config = get_model_doctype_json(self.__class__.__name__)
            return doctype_config.get("name", self.__class__.__name__)
        except Exception:
            return self.__class__.__name__.lower()

    def save(self, *args, **kwargs):
        # Set ID from config if not set
        if not self.id:
            self.id = self.get_config_based_id()
            
            # Verify singleton constraint
            if self.__class__.objects.exists():
                raise ValidationError(f"Only one instance of {self.__class__.__name__} is allowed.")
            
            self._just_created = True
            
        super().save(*args, **kwargs)
        self._just_created = False

    @classmethod
    def get_instance(cls):
        """
        Get or create the single instance using filter() approach.
        Automatically sets ID based on config name.
        """
        # Generate the singleton ID
        temp_instance = cls()
        instance_id = temp_instance.get_config_based_id()
        
        # Try to get existing instance using filter()
        instance = cls.objects.filter(id=instance_id).first()
        
        if instance:
            instance._just_created = False
            return instance
        
        # If no instance exists, create new one
        if cls.objects.exists():
            raise ValidationError(f"Only one instance of {cls.__name__} is allowed.")
        
        instance = cls(id=instance_id)
        instance._just_created = True
        instance.save()
        return instance

    def delete(self, *args, **kwargs):
        """Prevent deletion of the singleton instance"""
        raise ValidationError(f"Cannot delete singleton instance of {self.__class__.__name__}")

class SubmittableModel(BaseModel):
    """
    Abstract model for documents that can be submitted and cancelled,
    with field-level control over editable states and signal support.
    """
    DOCSTATUS_DRAFT = 0
    DOCSTATUS_SUBMITTED = 1
    DOCSTATUS_CANCELLED = 2
    
    DOCSTATUS_CHOICES = (
        (DOCSTATUS_DRAFT, 'Draft'),
        (DOCSTATUS_SUBMITTED, 'Submitted'),
        (DOCSTATUS_CANCELLED, 'Cancelled'),
    )
    
    docstatus = models.PositiveSmallIntegerField(
        choices=DOCSTATUS_CHOICES,
        default=DOCSTATUS_DRAFT,
        editable=False,
        help_text="0=Draft, 1=Submitted, 2=Cancelled"
    )
    
    class Meta:
        abstract = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_docstatus = self.docstatus if self.pk else None
    
    def clean(self):
        """Validate document status transitions and field modifications"""
        if self.pk:
            original = self.__class__.objects.get(pk=self.pk)
            
            # Prevent changing from submitted/cancelled back to draft
            if original.docstatus != self.DOCSTATUS_DRAFT and self.docstatus == self.DOCSTATUS_DRAFT:
                raise ValidationError("Cannot change status from Submitted/Cancelled back to Draft")
            
            # Prevent modifying cancelled documents entirely
            if original.docstatus == self.DOCSTATUS_CANCELLED:
                raise ValidationError("Cannot modify Cancelled documents")
            
            # For submitted documents, check field-level permissions
            if original.docstatus == self.DOCSTATUS_SUBMITTED:
                for field in self._meta.get_fields():
                    field_name = field.name
                    
                    # Skip system fields
                    if field_name in ['docstatus', 'id', 'created', 'modified']:
                        continue
                    
                    # Get the field object from the model
                    model_field = self._meta.get_field(field_name)
                    
                    # Check if field is allowed to be modified on submitted documents
                    allow_on_submit = getattr(model_field, 'allow_on_submit', False)
                    if allow_on_submit:
                        continue
                        
                    # Compare values
                    original_value = getattr(original, field_name)
                    current_value = getattr(self, field_name)
                    if original_value != current_value:
                        raise ValidationError(
                            f"Cannot modify field '{field_name}' on submitted document "
                            "unless explicitly allowed with allow_on_submit=True"
                        )
    
    def delete(self, *args, **kwargs):
        """Prevent deletion of submitted documents"""
        if self.docstatus == self.DOCSTATUS_SUBMITTED:
            raise ValidationError("Cannot delete Submitted documents")
        super().delete(*args, **kwargs)
    
    def submit(self):
        """Submit the document (change status to Submitted)"""
        if self.docstatus != self.DOCSTATUS_DRAFT:
            raise ValidationError("Only Draft documents can be submitted")
        
        # Trigger before_submit signal
        from core.signals import document_signals
        document_signals.before_submit.send(
            sender=self.__class__,
            instance=self
        )
        
        self.docstatus = self.DOCSTATUS_SUBMITTED
        self.save()
        
        # Trigger on_submit signal
        document_signals.on_submit.send(
            sender=self.__class__,
            instance=self
        )
    
    def cancel(self):
        """Cancel the document (change status to Cancelled)"""
        if self.docstatus != self.DOCSTATUS_SUBMITTED:
            raise ValidationError("Only Submitted documents can be cancelled")
        
        # Trigger before_cancel signal
        from core.signals import document_signals
        document_signals.before_cancel.send(
            sender=self.__class__,
            instance=self
        )
        
        self.docstatus = self.DOCSTATUS_CANCELLED
        self.save()
        
        # Trigger on_cancel signal
        document_signals.on_cancel.send(
            sender=self.__class__,
            instance=self
        )
    
    def save_draft(self):
        """Save draft with signal support"""
        from core.signals import document_signals
        document_signals.before_save_draft.send(
            sender=self.__class__,
            instance=self
        )
        
        self.save()
        
        document_signals.on_save_draft.send(
            sender=self.__class__,
            instance=self
        )
    
    def is_draft(self):
        return self.docstatus == self.DOCSTATUS_DRAFT
    
    def is_submitted(self):
        return self.docstatus == self.DOCSTATUS_SUBMITTED
    
    def is_cancelled(self):
        return self.docstatus == self.DOCSTATUS_CANCELLED



