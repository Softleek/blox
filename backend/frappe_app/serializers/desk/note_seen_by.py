from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.note_seen_by import NoteSeenBy

class NoteSeenBySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NoteSeenBy
        fields = '__all__'
