import django_filters as filters
from frappe_app.models.integrations.google_contacts import GoogleContacts

class GoogleContactsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GoogleContacts
        fields = ['id']

