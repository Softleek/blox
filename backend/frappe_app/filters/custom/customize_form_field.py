import django_filters as filters
from frappe_app.models.custom.customize_form_field import CustomizeFormField

class CustomizeFormFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CustomizeFormField
        fields = ['id']

