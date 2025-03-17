from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_template_field import WebTemplateField
from frappe_app.filters.website.web_template_field import WebTemplateFieldFilter
from frappe_app.serializers.website.web_template_field import WebTemplateFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebTemplateFieldViewSet(GenericViewSet):
    queryset = WebTemplateField.objects.all()
    filterset_class = WebTemplateFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebTemplateFieldSerializer

