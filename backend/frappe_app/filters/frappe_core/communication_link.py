import django_filters as filters
from frappe_app.models.frappe_core.communication_link import CommunicationLink

class CommunicationLinkFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CommunicationLink
        fields = ['id']

