from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.integrations.google_drive import GoogleDrive
from frappe_app.filters.integrations.google_drive import GoogleDriveFilter
from frappe_app.serializers.integrations.google_drive import GoogleDriveSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GoogleDriveViewSet(SingleInstanceViewSet):
    queryset = GoogleDrive.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = GoogleDriveSerializer

    filterset_class = GoogleDriveFilter
