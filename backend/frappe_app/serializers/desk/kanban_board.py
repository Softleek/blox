from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.kanban_board import KanbanBoard

class KanbanBoardSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = KanbanBoard
        fields = '__all__'
