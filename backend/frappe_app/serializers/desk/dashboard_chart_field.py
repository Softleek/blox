from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.dashboard_chart_field import DashboardChartField

class DashboardChartFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DashboardChartField
        fields = '__all__'
