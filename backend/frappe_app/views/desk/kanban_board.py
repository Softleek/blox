from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.kanban_board import KanbanBoard
from frappe_app.filters.desk.kanban_board import KanbanBoardFilter
from frappe_app.serializers.desk.kanban_board import KanbanBoardSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class KanbanBoardViewSet(GenericViewSet):
    queryset = KanbanBoard.objects.all()
    filterset_class = KanbanBoardFilter
    permission_classes = [HasGroupPermission]
    serializer_class = KanbanBoardSerializer

