import django_filters as filters
from frappe_app.models.frappe_core.audit_trail import AuditTrail

class AuditTrailFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AuditTrail
        fields = ['id']

