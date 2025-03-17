import django_filters as filters
from frappe_app.models.custom.property_setter import PropertySetter

class PropertySetterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PropertySetter
        fields = ['id']

