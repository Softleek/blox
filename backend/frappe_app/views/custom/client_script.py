from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.client_script import ClientScript
from frappe_app.filters.custom.client_script import ClientScriptFilter
from frappe_app.serializers.custom.client_script import ClientScriptSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ClientScriptViewSet(GenericViewSet):
    queryset = ClientScript.objects.all()
    filterset_class = ClientScriptFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ClientScriptSerializer

