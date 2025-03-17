from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_page_block import WebPageBlock
from frappe_app.filters.website.web_page_block import WebPageBlockFilter
from frappe_app.serializers.website.web_page_block import WebPageBlockSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebPageBlockViewSet(GenericViewSet):
    queryset = WebPageBlock.objects.all()
    filterset_class = WebPageBlockFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebPageBlockSerializer

