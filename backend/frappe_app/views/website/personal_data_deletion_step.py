from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.personal_data_deletion_step import PersonalDataDeletionStep
from frappe_app.filters.website.personal_data_deletion_step import PersonalDataDeletionStepFilter
from frappe_app.serializers.website.personal_data_deletion_step import PersonalDataDeletionStepSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PersonalDataDeletionStepViewSet(GenericViewSet):
    queryset = PersonalDataDeletionStep.objects.all()
    filterset_class = PersonalDataDeletionStepFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PersonalDataDeletionStepSerializer

