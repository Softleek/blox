
from .get_model_details import get_model_doctype_json



def autoname(instance):
    """
    Get the naming rule for a model instance. Defaults to a random string if none is defined.

    Args:
        instance (models.Model): The model instance.

    Returns:
        str: The naming rule or default.
    """
    model_name = instance.__class__.__name__
    return get_model_doctype_json(model_name)



