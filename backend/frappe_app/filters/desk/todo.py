import django_filters as filters
from frappe_app.models.desk.todo import ToDo

class ToDoFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ToDo
        fields = ['id']

