import django_filters as filters
from frappe_app.models.desk.global_search_settings import GlobalSearchSettings

class GlobalSearchSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GlobalSearchSettings
        fields = ['id']

