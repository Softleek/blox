from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.route_history import RouteHistory
from frappe_app.filters.desk.route_history import RouteHistoryFilter
from frappe_app.serializers.desk.route_history import RouteHistorySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RouteHistoryViewSet(GenericViewSet):
    queryset = RouteHistory.objects.all()
    filterset_class = RouteHistoryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RouteHistorySerializer

