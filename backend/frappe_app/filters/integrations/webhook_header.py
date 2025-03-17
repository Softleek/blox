import django_filters as filters
from frappe_app.models.integrations.webhook_header import WebhookHeader

class WebhookHeaderFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebhookHeader
        fields = ['id']

