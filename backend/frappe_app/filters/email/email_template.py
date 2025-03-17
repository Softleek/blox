import django_filters as filters
from frappe_app.models.email.email_template import EmailTemplate

class EmailTemplateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailTemplate
        fields = ['id']

