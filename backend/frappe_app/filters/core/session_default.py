import django_filters as filters
from frappe_app.models.core.session_default import SessionDefault

class SessionDefaultFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SessionDefault
        fields = ['id']

