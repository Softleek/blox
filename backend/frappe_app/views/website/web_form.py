from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.web_form import WebForm
from frappe_app.filters.website.web_form import WebFormFilter
from frappe_app.serializers.website.web_form import WebFormSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebFormViewSet(GenericViewSet):
    queryset = WebForm.objects.all()
    filterset_class = WebFormFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebFormSerializer

