from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.server_script import ServerScript
from frappe_app.filters.frappe_core.server_script import ServerScriptFilter
from frappe_app.serializers.frappe_core.server_script import ServerScriptSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ServerScriptViewSet(GenericViewSet):
    queryset = ServerScript.objects.all()
    filterset_class = ServerScriptFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ServerScriptSerializer

