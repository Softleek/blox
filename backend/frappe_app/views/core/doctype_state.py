from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.doctype_state import DocTypeState
from frappe_app.filters.core.doctype_state import DocTypeStateFilter
from frappe_app.serializers.core.doctype_state import DocTypeStateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeStateViewSet(GenericViewSet):
    queryset = DocTypeState.objects.all()
    filterset_class = DocTypeStateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeStateSerializer

