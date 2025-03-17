from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.personal_data_download_request import PersonalDataDownloadRequest
from frappe_app.filters.website.personal_data_download_request import PersonalDataDownloadRequestFilter
from frappe_app.serializers.website.personal_data_download_request import PersonalDataDownloadRequestSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PersonalDataDownloadRequestViewSet(GenericViewSet):
    queryset = PersonalDataDownloadRequest.objects.all()
    filterset_class = PersonalDataDownloadRequestFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PersonalDataDownloadRequestSerializer

