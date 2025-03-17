import django_filters as filters
from frappe_app.models.desk.note_seen_by import NoteSeenBy

class NoteSeenByFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NoteSeenBy
        fields = ['id']

