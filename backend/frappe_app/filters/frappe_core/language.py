import django_filters as filters
from frappe_app.models.frappe_core.language import Language

class LanguageFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Language
        fields = ['id']

