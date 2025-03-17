import django_filters as filters
from frappe_app.models.core.communication import Communication

class CommunicationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Communication
        fields = ['id']

