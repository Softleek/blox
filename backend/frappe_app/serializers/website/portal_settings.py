from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.portal_settings import PortalSettings

class PortalSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PortalSettings
        fields = '__all__'
