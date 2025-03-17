from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.dashboard_chart_link import DashboardChartLink

class DashboardChartLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DashboardChartLink
        fields = '__all__'
