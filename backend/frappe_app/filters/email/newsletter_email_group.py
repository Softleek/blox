import django_filters as filters
from frappe_app.models.email.newsletter_email_group import NewsletterEmailGroup

class NewsletterEmailGroupFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NewsletterEmailGroup
        fields = ['id']

