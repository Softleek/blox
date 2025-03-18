import django_filters as filters
from frappe_app.models.frappe_core.domain import Domain

class DomainFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Domain
        fields = ['id']

