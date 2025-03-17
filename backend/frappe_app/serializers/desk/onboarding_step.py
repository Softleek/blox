from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.onboarding_step import OnboardingStep

class OnboardingStepSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OnboardingStep
        fields = '__all__'
