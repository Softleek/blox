from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.session_default import SessionDefault
from frappe_app.filters.frappe_core.session_default import SessionDefaultFilter
from frappe_app.serializers.frappe_core.session_default import SessionDefaultSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SessionDefaultViewSet(GenericViewSet):
    queryset = SessionDefault.objects.all()
    filterset_class = SessionDefaultFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SessionDefaultSerializer

