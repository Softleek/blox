from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_form_list_column import WebFormListColumn
from frappe_app.filters.website.web_form_list_column import WebFormListColumnFilter
from frappe_app.serializers.website.web_form_list_column import WebFormListColumnSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebFormListColumnViewSet(GenericViewSet):
    queryset = WebFormListColumn.objects.all()
    filterset_class = WebFormListColumnFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebFormListColumnSerializer

