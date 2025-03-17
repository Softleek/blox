from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.kanban_board_column import KanbanBoardColumn
from frappe_app.filters.desk.kanban_board_column import KanbanBoardColumnFilter
from frappe_app.serializers.desk.kanban_board_column import KanbanBoardColumnSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class KanbanBoardColumnViewSet(GenericViewSet):
    queryset = KanbanBoardColumn.objects.all()
    filterset_class = KanbanBoardColumnFilter
    permission_classes = [HasGroupPermission]
    serializer_class = KanbanBoardColumnSerializer

