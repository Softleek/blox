from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.auto_repeat import AutoRepeat

class AutoRepeatSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AutoRepeat
        fields = '__all__'
