from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.sms_parameter import SMSParameter

class SMSParameterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SMSParameter
        fields = '__all__'
