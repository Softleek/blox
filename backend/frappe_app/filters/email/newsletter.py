import django_filters as filters
from frappe_app.models.email.newsletter import Newsletter

class NewsletterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Newsletter
        fields = ['id']

