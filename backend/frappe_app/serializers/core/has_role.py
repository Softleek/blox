from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.has_role import HasRole

class HasRoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = HasRole
        fields = '__all__'
