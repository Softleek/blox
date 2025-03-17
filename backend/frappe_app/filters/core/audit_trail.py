import django_filters as filters
from frappe_app.models.core.audit_trail import AuditTrail

class AuditTrailFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AuditTrail
        fields = ['id']

