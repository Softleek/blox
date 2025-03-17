from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.auto_email_report import AutoEmailReport

class AutoEmailReportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AutoEmailReport
        fields = '__all__'
