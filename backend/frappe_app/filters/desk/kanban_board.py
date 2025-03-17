import django_filters as filters
from frappe_app.models.desk.kanban_board import KanbanBoard

class KanbanBoardFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = KanbanBoard
        fields = ['id']

