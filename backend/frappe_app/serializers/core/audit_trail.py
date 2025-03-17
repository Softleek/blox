from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.audit_trail import AuditTrail

class AuditTrailSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AuditTrail
        fields = '__all__'
