import django_filters as filters
from frappe_app.models.contacts.salutation import Salutation

class SalutationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Salutation
        fields = ['id']

