from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.recorder_query import RecorderQuery

class RecorderQuerySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RecorderQuery
        fields = '__all__'
