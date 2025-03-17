import django_filters as filters
from frappe_app.models.integrations.integration_request import IntegrationRequest

class IntegrationRequestFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = IntegrationRequest
        fields = ['id']

