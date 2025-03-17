from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.note import Note

class NoteSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
