from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.transaction_log import TransactionLog
from frappe_app.filters.core.transaction_log import TransactionLogFilter
from frappe_app.serializers.core.transaction_log import TransactionLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TransactionLogViewSet(GenericViewSet):
    queryset = TransactionLog.objects.all()
    filterset_class = TransactionLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TransactionLogSerializer

