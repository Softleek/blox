from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.salutation import Salutation
from frappe_app.filters.contacts.salutation import SalutationFilter
from frappe_app.serializers.contacts.salutation import SalutationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SalutationViewSet(GenericViewSet):
    queryset = Salutation.objects.all()
    filterset_class = SalutationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SalutationSerializer

