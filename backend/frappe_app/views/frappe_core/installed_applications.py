from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.installed_applications import InstalledApplications
from frappe_app.filters.frappe_core.installed_applications import InstalledApplicationsFilter
from frappe_app.serializers.frappe_core.installed_applications import InstalledApplicationsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class InstalledApplicationsViewSet(SingleInstanceViewSet):
    queryset = InstalledApplications.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = InstalledApplicationsSerializer

    filterset_class = InstalledApplicationsFilter
