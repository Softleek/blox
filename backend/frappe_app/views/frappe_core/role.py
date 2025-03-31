from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.role import Role
from frappe_app.filters.frappe_core.role import RoleFilter
from frappe_app.serializers.frappe_core.role import RoleSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RoleViewSet(GenericViewSet):
    queryset = Role.objects.all()
    filterset_class = RoleFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RoleSerializer

    filterset_class = RoleFilter
