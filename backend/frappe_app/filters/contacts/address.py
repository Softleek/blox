import django_filters as filters
from frappe_app.models.contacts.address import Address

class AddressFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Address
        fields = ['id']

