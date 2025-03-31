from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.audit_trail import AuditTrail
from frappe_app.filters.frappe_core.audit_trail import AuditTrailFilter
from frappe_app.serializers.frappe_core.audit_trail import AuditTrailSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AuditTrailViewSet(SingleInstanceViewSet):
    queryset = AuditTrail.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = AuditTrailSerializer

    filterset_class = AuditTrailFilter
