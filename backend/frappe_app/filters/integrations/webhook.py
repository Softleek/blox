import django_filters as filters
from frappe_app.models.integrations.webhook import Webhook

class WebhookFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Webhook
        fields = ['id']

