import django_filters as filters
from frappe_app.models.integrations.connected_app import ConnectedApp

class ConnectedAppFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ConnectedApp
        fields = ['id']

