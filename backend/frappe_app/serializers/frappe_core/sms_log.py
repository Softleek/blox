from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.sms_log import SMSLog

class SMSLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SMSLog
        fields = '__all__'
