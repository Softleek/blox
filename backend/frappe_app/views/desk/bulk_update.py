from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.bulk_update import BulkUpdate
from frappe_app.filters.desk.bulk_update import BulkUpdateFilter
from frappe_app.serializers.desk.bulk_update import BulkUpdateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BulkUpdateViewSet(GenericViewSet):
    queryset = BulkUpdate.objects.all()
    filterset_class = BulkUpdateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BulkUpdateSerializer

