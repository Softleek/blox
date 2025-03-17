import django_filters as filters
from frappe_app.models.contacts.contact_phone import ContactPhone

class ContactPhoneFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ContactPhone
        fields = ['id']

