import django_filters as filters
from frappe_app.models.email.email_group import EmailGroup

class EmailGroupFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailGroup
        fields = ['id']

