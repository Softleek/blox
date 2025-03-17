from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.view_log import ViewLog

class ViewLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ViewLog
        fields = '__all__'
