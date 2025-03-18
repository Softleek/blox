from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.submission_queue import SubmissionQueue
from frappe_app.filters.frappe_core.submission_queue import SubmissionQueueFilter
from frappe_app.serializers.frappe_core.submission_queue import SubmissionQueueSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SubmissionQueueViewSet(GenericViewSet):
    queryset = SubmissionQueue.objects.all()
    filterset_class = SubmissionQueueFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SubmissionQueueSerializer

