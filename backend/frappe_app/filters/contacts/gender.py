import django_filters as filters
from frappe_app.models.contacts.gender import Gender

class GenderFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Gender
        fields = ['id']

