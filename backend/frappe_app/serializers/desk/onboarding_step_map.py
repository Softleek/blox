from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.onboarding_step_map import OnboardingStepMap

class OnboardingStepMapSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OnboardingStepMap
        fields = '__all__'
