import django_filters as filters
from frappe_app.models.core.language import Language

class LanguageFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Language
        fields = ['id']

