from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.report_column import ReportColumn

class ReportColumnSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ReportColumn
        fields = '__all__'
