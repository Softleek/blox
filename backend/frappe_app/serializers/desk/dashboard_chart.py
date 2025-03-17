from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.dashboard_chart import DashboardChart

class DashboardChartSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DashboardChart
        fields = '__all__'
