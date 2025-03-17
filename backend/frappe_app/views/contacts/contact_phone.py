from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.contact_phone import ContactPhone
from frappe_app.filters.contacts.contact_phone import ContactPhoneFilter
from frappe_app.serializers.contacts.contact_phone import ContactPhoneSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ContactPhoneViewSet(GenericViewSet):
    queryset = ContactPhone.objects.all()
    filterset_class = ContactPhoneFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ContactPhoneSerializer

