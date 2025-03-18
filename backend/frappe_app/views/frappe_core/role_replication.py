from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.role_replication import RoleReplication
from frappe_app.filters.frappe_core.role_replication import RoleReplicationFilter
from frappe_app.serializers.frappe_core.role_replication import RoleReplicationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RoleReplicationViewSet(GenericViewSet):
    queryset = RoleReplication.objects.all()
    filterset_class = RoleReplicationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RoleReplicationSerializer

