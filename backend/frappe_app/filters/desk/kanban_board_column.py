import django_filters as filters
from frappe_app.models.desk.kanban_board_column import KanbanBoardColumn

class KanbanBoardColumnFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = KanbanBoardColumn
        fields = ['id']

