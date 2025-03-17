import django_filters as filters
from frappe_app.models.integrations.webhook_request_log import WebhookRequestLog

class WebhookRequestLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebhookRequestLog
        fields = ['id']

