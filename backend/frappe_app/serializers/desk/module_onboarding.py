from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.module_onboarding import ModuleOnboarding

class ModuleOnboardingSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ModuleOnboarding
        fields = '__all__'
