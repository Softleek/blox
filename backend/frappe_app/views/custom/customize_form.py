from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.customize_form import CustomizeForm
from frappe_app.filters.custom.customize_form import CustomizeFormFilter
from frappe_app.serializers.custom.customize_form import CustomizeFormSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomizeFormViewSet(GenericViewSet):
    queryset = CustomizeForm.objects.all()
    filterset_class = CustomizeFormFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomizeFormSerializer

