import django_filters as filters
from frappe_app.models.email.newsletter_attachment import NewsletterAttachment

class NewsletterAttachmentFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NewsletterAttachment
        fields = ['id']

