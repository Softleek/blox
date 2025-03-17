from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.google_contacts import GoogleContacts
from frappe_app.filters.integrations.google_contacts import GoogleContactsFilter
from frappe_app.serializers.integrations.google_contacts import GoogleContactsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GoogleContactsViewSet(GenericViewSet):
    queryset = GoogleContacts.objects.all()
    filterset_class = GoogleContactsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GoogleContactsSerializer

