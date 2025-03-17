import django_filters as filters
from frappe_app.models.core.server_script import ServerScript

class ServerScriptFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ServerScript
        fields = ['id']

