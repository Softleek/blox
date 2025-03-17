from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.recorder_suggested_index import RecorderSuggestedIndex

class RecorderSuggestedIndexSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = RecorderSuggestedIndex
        fields = '__all__'
