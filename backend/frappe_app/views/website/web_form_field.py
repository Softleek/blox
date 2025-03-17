from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_form_field import WebFormField
from frappe_app.filters.website.web_form_field import WebFormFieldFilter
from frappe_app.serializers.website.web_form_field import WebFormFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebFormFieldViewSet(GenericViewSet):
    queryset = WebFormField.objects.all()
    filterset_class = WebFormFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebFormFieldSerializer

