from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.version import Version
from frappe_app.filters.frappe_core.version import VersionFilter
from frappe_app.serializers.frappe_core.version import VersionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class VersionViewSet(GenericViewSet):
    queryset = Version.objects.all()
    filterset_class = VersionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = VersionSerializer

