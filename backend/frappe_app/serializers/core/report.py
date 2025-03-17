from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.report import Report

class ReportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'
