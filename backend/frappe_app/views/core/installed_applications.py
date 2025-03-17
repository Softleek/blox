from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.installed_applications import InstalledApplications
from frappe_app.filters.core.installed_applications import InstalledApplicationsFilter
from frappe_app.serializers.core.installed_applications import InstalledApplicationsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class InstalledApplicationsViewSet(GenericViewSet):
    queryset = InstalledApplications.objects.all()
    filterset_class = InstalledApplicationsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = InstalledApplicationsSerializer

