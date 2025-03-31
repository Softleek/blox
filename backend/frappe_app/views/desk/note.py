from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.note import Note
from frappe_app.filters.desk.note import NoteFilter
from frappe_app.serializers.desk.note import NoteSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NoteViewSet(GenericViewSet):
    queryset = Note.objects.all()
    filterset_class = NoteFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NoteSerializer

    filterset_class = NoteFilter
