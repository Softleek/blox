from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_template import WebTemplate
from frappe_app.filters.website.web_template import WebTemplateFilter
from frappe_app.serializers.website.web_template import WebTemplateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebTemplateViewSet(GenericViewSet):
    queryset = WebTemplate.objects.all()
    filterset_class = WebTemplateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebTemplateSerializer

