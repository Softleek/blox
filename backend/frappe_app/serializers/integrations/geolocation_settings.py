from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.geolocation_settings import GeolocationSettings

class GeolocationSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = GeolocationSettings
        fields = '__all__'
