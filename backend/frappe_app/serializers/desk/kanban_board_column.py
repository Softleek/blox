from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.kanban_board_column import KanbanBoardColumn

class KanbanBoardColumnSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = KanbanBoardColumn
        fields = '__all__'
