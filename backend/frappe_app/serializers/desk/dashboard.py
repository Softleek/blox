from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.dashboard import Dashboard

class DashboardSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Dashboard
        fields = '__all__'
