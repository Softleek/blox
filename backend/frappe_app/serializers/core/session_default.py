from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.session_default import SessionDefault

class SessionDefaultSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SessionDefault
        fields = '__all__'
