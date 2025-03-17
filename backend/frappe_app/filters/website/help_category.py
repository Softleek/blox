import django_filters as filters
from frappe_app.models.website.help_category import HelpCategory

class HelpCategoryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = HelpCategory
        fields = ['id']

