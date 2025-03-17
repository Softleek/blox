import django_filters as filters
from frappe_app.models.contacts.contact import Contact

class ContactFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Contact
        fields = ['id']

