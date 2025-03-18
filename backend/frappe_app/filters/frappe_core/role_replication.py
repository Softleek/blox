import django_filters as filters
from frappe_app.models.frappe_core.role_replication import RoleReplication

class RoleReplicationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = RoleReplication
        fields = ['id']

