import django_filters as filters
from frappe_app.models.desk.note import Note

class NoteFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Note
        fields = ['id']

