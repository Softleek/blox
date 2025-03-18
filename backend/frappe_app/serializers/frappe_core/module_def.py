from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.module_def import ModuleDef

class ModuleDefSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ModuleDef
        fields = '__all__'
