from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.route_history import RouteHistory

class RouteHistorySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RouteHistory
        fields = '__all__'
