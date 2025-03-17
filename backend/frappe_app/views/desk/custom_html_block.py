from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.custom_html_block import CustomHTMLBlock
from frappe_app.filters.desk.custom_html_block import CustomHTMLBlockFilter
from frappe_app.serializers.desk.custom_html_block import CustomHTMLBlockSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomHTMLBlockViewSet(GenericViewSet):
    queryset = CustomHTMLBlock.objects.all()
    filterset_class = CustomHTMLBlockFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomHTMLBlockSerializer

