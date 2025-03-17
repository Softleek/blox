from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.social.energy_point_rule import EnergyPointRule

class EnergyPointRuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EnergyPointRule
        fields = '__all__'
