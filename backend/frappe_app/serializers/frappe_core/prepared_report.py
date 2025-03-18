from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.prepared_report import PreparedReport

class PreparedReportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PreparedReport
        fields = '__all__'
