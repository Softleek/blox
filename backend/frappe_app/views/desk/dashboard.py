from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard import Dashboard
from frappe_app.filters.desk.dashboard import DashboardFilter
from frappe_app.serializers.desk.dashboard import DashboardSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardViewSet(GenericViewSet):
    queryset = Dashboard.objects.all()
    filterset_class = DashboardFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardSerializer

