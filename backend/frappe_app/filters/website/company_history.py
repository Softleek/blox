import django_filters as filters
from frappe_app.models.website.company_history import CompanyHistory

class CompanyHistoryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CompanyHistory
        fields = ['id']

