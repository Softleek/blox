from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.contact_email import ContactEmail
from frappe_app.filters.contacts.contact_email import ContactEmailFilter
from frappe_app.serializers.contacts.contact_email import ContactEmailSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ContactEmailViewSet(GenericViewSet):
    queryset = ContactEmail.objects.all()
    filterset_class = ContactEmailFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ContactEmailSerializer

