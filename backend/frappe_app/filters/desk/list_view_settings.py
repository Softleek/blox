import django_filters as filters
from frappe_app.models.desk.list_view_settings import ListViewSettings

class ListViewSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ListViewSettings
        fields = ['id']

