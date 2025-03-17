import django_filters as filters
from frappe_app.models.contacts.contact_email import ContactEmail

class ContactEmailFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ContactEmail
        fields = ['id']

