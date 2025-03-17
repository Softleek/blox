from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.personal_data_deletion_request import PersonalDataDeletionRequest
from frappe_app.filters.website.personal_data_deletion_request import PersonalDataDeletionRequestFilter
from frappe_app.serializers.website.personal_data_deletion_request import PersonalDataDeletionRequestSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PersonalDataDeletionRequestViewSet(GenericViewSet):
    queryset = PersonalDataDeletionRequest.objects.all()
    filterset_class = PersonalDataDeletionRequestFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PersonalDataDeletionRequestSerializer

