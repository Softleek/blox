from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.dashboard_settings import DashboardSettings
from frappe_app.filters.desk.dashboard_settings import DashboardSettingsFilter
from frappe_app.serializers.desk.dashboard_settings import DashboardSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DashboardSettingsViewSet(GenericViewSet):
    queryset = DashboardSettings.objects.all()
    filterset_class = DashboardSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DashboardSettingsSerializer

