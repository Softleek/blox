from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.social.energy_point_log import EnergyPointLog

class EnergyPointLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EnergyPointLog
        fields = '__all__'
