import django_filters as filters
from frappe_app.models.integrations.slack_webhook_url import SlackWebhookURL

class SlackWebhookURLFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SlackWebhookURL
        fields = ['id']

