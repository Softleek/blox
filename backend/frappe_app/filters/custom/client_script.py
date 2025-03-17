import django_filters as filters
from frappe_app.models.custom.client_script import ClientScript

class ClientScriptFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ClientScript
        fields = ['id']

