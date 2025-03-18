from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.audit_trail import AuditTrail
from frappe_app.filters.frappe_core.audit_trail import AuditTrailFilter
from frappe_app.serializers.frappe_core.audit_trail import AuditTrailSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AuditTrailViewSet(GenericViewSet):
    queryset = AuditTrail.objects.all()
    filterset_class = AuditTrailFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AuditTrailSerializer

