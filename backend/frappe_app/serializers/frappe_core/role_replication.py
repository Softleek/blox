from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.role_replication import RoleReplication

class RoleReplicationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RoleReplication
        fields = '__all__'
