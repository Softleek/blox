from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.company_history import CompanyHistory
from frappe_app.filters.website.company_history import CompanyHistoryFilter
from frappe_app.serializers.website.company_history import CompanyHistorySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CompanyHistoryViewSet(GenericViewSet):
    queryset = CompanyHistory.objects.all()
    filterset_class = CompanyHistoryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CompanyHistorySerializer

