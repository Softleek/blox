import django_filters as filters
from frappe_app.models.frappe_core.custom_docperm import CustomDocPerm

class CustomDocPermFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CustomDocPerm
        fields = ['id']

