from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.contact import Contact
from frappe_app.filters.contacts.contact import ContactFilter
from frappe_app.serializers.contacts.contact import ContactSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ContactViewSet(GenericViewSet):
    queryset = Contact.objects.all()
    filterset_class = ContactFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ContactSerializer

