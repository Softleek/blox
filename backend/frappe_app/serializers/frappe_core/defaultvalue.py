from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.defaultvalue import DefaultValue

class DefaultValueSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DefaultValue
        fields = '__all__'
