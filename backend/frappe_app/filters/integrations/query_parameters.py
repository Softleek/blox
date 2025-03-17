import django_filters as filters
from frappe_app.models.integrations.query_parameters import QueryParameters

class QueryParametersFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = QueryParameters
        fields = ['id']

