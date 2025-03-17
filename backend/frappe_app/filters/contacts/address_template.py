import django_filters as filters
from frappe_app.models.contacts.address_template import AddressTemplate

class AddressTemplateFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AddressTemplate
        fields = ['id']

