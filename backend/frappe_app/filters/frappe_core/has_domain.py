import django_filters as filters
from frappe_app.models.frappe_core.has_domain import HasDomain

class HasDomainFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = HasDomain
        fields = ['id']

