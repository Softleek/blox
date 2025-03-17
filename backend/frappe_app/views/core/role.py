from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.role import Role
from frappe_app.filters.core.role import RoleFilter
from frappe_app.serializers.core.role import RoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RoleViewSet(GenericViewSet):
    queryset = Role.objects.all()
    filterset_class = RoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RoleSerializer

