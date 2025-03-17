from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.module_profile import ModuleProfile

class ModuleProfileSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ModuleProfile
        fields = '__all__'
