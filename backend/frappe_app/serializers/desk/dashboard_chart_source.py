from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.dashboard_chart_source import DashboardChartSource

class DashboardChartSourceSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DashboardChartSource
        fields = '__all__'
