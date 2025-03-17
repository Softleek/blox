from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.desktop_icon import DesktopIcon
from frappe_app.filters.desk.desktop_icon import DesktopIconFilter
from frappe_app.serializers.desk.desktop_icon import DesktopIconSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DesktopIconViewSet(GenericViewSet):
    queryset = DesktopIcon.objects.all()
    filterset_class = DesktopIconFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DesktopIconSerializer

