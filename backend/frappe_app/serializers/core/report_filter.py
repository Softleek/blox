from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.report_filter import ReportFilter

class ReportFilterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ReportFilter
        fields = '__all__'
