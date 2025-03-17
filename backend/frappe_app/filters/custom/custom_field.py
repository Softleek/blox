import django_filters as filters
from frappe_app.models.custom.custom_field import CustomField

class CustomFieldFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')
    dt = filters.CharFilter(lookup_expr='icontains', label='Dt')
    label = filters.CharFilter(lookup_expr='icontains', label='Label')
    fieldtype = filters.CharFilter(lookup_expr='icontains', label='Fieldtype')

    class Meta:
        model = CustomField
        fields = ['id', 'dt', 'label', 'fieldtype']

