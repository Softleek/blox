import django_filters as filters
from frappe_app.models.desk.route_history import RouteHistory

class RouteHistoryFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RouteHistory
        fields = ['id']

