from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.event import Event

class EventSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
