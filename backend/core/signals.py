from threading import local

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .utils.get_model_details import get_model_doctype_json
from .utils.naming_manager import NamingManager
from django.dispatch import Signal
_request_local = local()


def get_current_user():
    return getattr(_request_local, "user", "system")
# Custom signals for document lifecycle events


class DocumentSignals:
    def __init__(self):
        self.before_submit = Signal()
        self.on_submit = Signal()
        self.before_cancel = Signal()
        self.on_cancel = Signal()
        self.before_save_draft = Signal()
        self.on_save_draft = Signal()
        
        # Register additional signals later if needed
        self._signals = {
            'before_submit': self.before_submit,
            'on_submit': self.on_submit,
            'before_cancel': self.before_cancel,
            'on_cancel': self.on_cancel,
            'before_save_draft': self.before_save_draft,
            'on_save_draft': self.on_save_draft,
        }
    
    def register(self, signal_name):
        """Dynamically add new signals"""
        if signal_name not in self._signals:
            new_signal = Signal()
            self._signals[signal_name] = new_signal
            setattr(self, signal_name, new_signal)
            return new_signal
        return self._signals[signal_name]

# Global instance
document_signals = DocumentSignals()

# Django-style receiver decorator
def receiver(signal, **kwargs):
    def _decorator(func):
        if isinstance(signal, Signal):
            signal.connect(func, **kwargs)
        return func
    return _decorator

@receiver(pre_save)
def generate_name_for_model(sender, instance, **kwargs):
    """
    Pre-save signal to generate a name for models.
    Skips certain models like 'Token' that don't require name generation.
    """
    SKIP_MODELS = {
        "Token",
        "Session",
        "LogEntry",
        "Group",
        "Permission",
        "UserIPAddress",
        "OTP",
        "User",
        "ChangeLog",
    }

    if sender.__name__ in SKIP_MODELS:
        return

    model_name = instance.__class__.__name__
    doctype_config = get_model_doctype_json(model_name)
    naming_manager = NamingManager(instance, doctype_config)
    
    is_single = str((doctype_config or {}).get("issingle")).lower() in ("1", "true")

    if doctype_config and doctype_config.get("fields"):
        for field in doctype_config.get("fields", []):
            fieldname = field.get("fieldname")
            fieldtype = field.get("fieldtype")
            format_value = field.get("format")

            if format_value:
                instance.__dict__[fieldname] = naming_manager.generate_code(
                    fieldname, format_value
                )
    
    if not getattr(instance, "created", None):
        if is_single:
            instance.id = doctype_config.get("name", model_name)
        else:
            id = naming_manager.generate_name()
            if id:
                instance.id = id

    if doctype_config and doctype_config.get("fields"):
        for field in doctype_config.get("fields", []):
            fieldname = field.get("fieldname")
            fieldtype = field.get("fieldtype")
            format_value = field.get("format")

            if fieldtype in ["Barcode", "QR Code"]:
                options = field.get("options", "{id}")
                code = naming_manager.generate_code(fieldname, options)
                instance.__dict__[fieldname] = code

    if (
        getattr(instance, "created", None)
        and doctype_config
        and doctype_config.get("track_changes") == (True or "1")
    ):
        track_changes_after_save(sender, instance, **kwargs)


def track_changes_after_save(sender, instance, **kwargs):
    model_name = sender.__name__
    object_id = str(instance.pk)
    changes = {}

    if kwargs.get("created", False):
        changes = {
            field.name: getattr(instance, field.name) for field in sender._meta.fields
        }
    else:
        old_instance = sender.objects.get(pk=instance.pk)
        old_values = {
            field.name: getattr(old_instance, field.name)
            for field in sender._meta.fields
        }
        new_values = {
            field.name: getattr(instance, field.name) for field in sender._meta.fields
        }

        for field, old_value in old_values.items():
            if field in ["modified", "modified_at"]:
                continue
            new_value = new_values.get(field)
            if old_value != new_value:
                changes[field] = {"old": str(old_value), "new": str(new_value)}
    if changes:
        from core.models import ChangeLog

        ChangeLog.objects.create(
            id=generate_uuid(),
            model_name=model_name,
            object_id=object_id,
            changes=changes,
            user=get_current_user() or "system",
        )


def generate_uuid():
    import uuid
    return str(uuid.uuid4())

# from frappe_mpsa_payments_app.models import MpesaExpressRequest

# @receiver(document_signals.before_submit, sender=MpesaExpressRequest)
# def my_handler(sender, instance, **kwargs):
#     print("-------------------------------------------")
#     print("Before submit signal received!")
#     print(f"Instance: {instance}")
#     print(f"Sender: {sender}")

#     # Change the status to "Failed" before submission
#     instance.status = "Failed"
#     instance.save(update_fields=["status"])