from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.event_participants import EventParticipants

class EventParticipantsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EventParticipants
        fields = '__all__'
