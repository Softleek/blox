from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.note_seen_by import NoteSeenBy
from frappe_app.filters.desk.note_seen_by import NoteSeenByFilter
from frappe_app.serializers.desk.note_seen_by import NoteSeenBySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NoteSeenByViewSet(GenericViewSet):
    queryset = NoteSeenBy.objects.all()
    filterset_class = NoteSeenByFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NoteSeenBySerializer

