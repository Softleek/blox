import django_filters as filters
from frappe_app.models.integrations.webhook_data import WebhookData

class WebhookDataFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebhookData
        fields = ['id']

