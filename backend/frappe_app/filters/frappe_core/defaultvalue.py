import django_filters as filters
from frappe_app.models.frappe_core.defaultvalue import DefaultValue

class DefaultValueFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DefaultValue
        fields = ['id']

