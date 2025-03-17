from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.onboarding_permission import OnboardingPermission

class OnboardingPermissionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = OnboardingPermission
        fields = '__all__'
