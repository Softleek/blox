from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.ldap_group_mapping import LDAPGroupMapping

class LDAPGroupMappingSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = LDAPGroupMapping
        fields = '__all__'
