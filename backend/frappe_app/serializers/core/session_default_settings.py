from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.session_default_settings import SessionDefaultSettings

class SessionDefaultSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SessionDefaultSettings
        fields = '__all__'
