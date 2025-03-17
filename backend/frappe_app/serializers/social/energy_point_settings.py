from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.social.energy_point_settings import EnergyPointSettings

class EnergyPointSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EnergyPointSettings
        fields = '__all__'
