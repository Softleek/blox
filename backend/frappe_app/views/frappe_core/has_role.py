from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.has_role import HasRole
from frappe_app.filters.frappe_core.has_role import HasRoleFilter
from frappe_app.serializers.frappe_core.has_role import HasRoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class HasRoleViewSet(GenericViewSet):
    queryset = HasRole.objects.all()
    filterset_class = HasRoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = HasRoleSerializer

