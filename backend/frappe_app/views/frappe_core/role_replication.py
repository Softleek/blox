from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.role_replication import RoleReplication
from frappe_app.filters.frappe_core.role_replication import RoleReplicationFilter
from frappe_app.serializers.frappe_core.role_replication import RoleReplicationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RoleReplicationViewSet(SingleInstanceViewSet):
    queryset = RoleReplication.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = RoleReplicationSerializer

    filterset_class = RoleReplicationFilter
