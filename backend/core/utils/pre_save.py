from django.db.models.signals import pre_save
from django.dispatch import receiver
from .naming_manager import NamingManager
from .get_model_details import get_model_doctype_json
from .data_validation import validate_model_data  # Import the validation function

@receiver(pre_save)
def generate_name_for_model(sender, instance, **kwargs):
    """
    Pre-save signal to generate a name for models.
    Assumes the instance has a `doctype_config` attribute.
    """
    model_name = instance.__class__.__name__
    doctype_config = get_model_doctype_json(model_name)

    # Validate the instance data
    # validate_model_data(instance)

    if not instance.name:  # Only generate if name is not set
        naming_manager = NamingManager(instance, doctype_config)
        instance.name = naming_manager.generate_name()
