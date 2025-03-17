from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.recorder import Recorder

class RecorderSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Recorder
        fields = '__all__'
