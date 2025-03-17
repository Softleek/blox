from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.global_search_doctype import GlobalSearchDocType
from frappe_app.filters.desk.global_search_doctype import GlobalSearchDocTypeFilter
from frappe_app.serializers.desk.global_search_doctype import GlobalSearchDocTypeSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GlobalSearchDocTypeViewSet(GenericViewSet):
    queryset = GlobalSearchDocType.objects.all()
    filterset_class = GlobalSearchDocTypeFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GlobalSearchDocTypeSerializer

