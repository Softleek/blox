from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.installed_application import InstalledApplication
from frappe_app.filters.frappe_core.installed_application import InstalledApplicationFilter
from frappe_app.serializers.frappe_core.installed_application import InstalledApplicationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class InstalledApplicationViewSet(GenericViewSet):
    queryset = InstalledApplication.objects.all()
    filterset_class = InstalledApplicationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = InstalledApplicationSerializer

