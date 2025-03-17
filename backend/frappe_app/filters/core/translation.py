import django_filters as filters
from frappe_app.models.core.translation import Translation

class TranslationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Translation
        fields = ['id']

