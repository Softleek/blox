from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.list_view_settings import ListViewSettings
from frappe_app.filters.desk.list_view_settings import ListViewSettingsFilter
from frappe_app.serializers.desk.list_view_settings import ListViewSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ListViewSettingsViewSet(GenericViewSet):
    queryset = ListViewSettings.objects.all()
    filterset_class = ListViewSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ListViewSettingsSerializer

