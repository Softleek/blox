from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.customize_form_field import CustomizeFormField
from frappe_app.filters.custom.customize_form_field import CustomizeFormFieldFilter
from frappe_app.serializers.custom.customize_form_field import CustomizeFormFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomizeFormFieldViewSet(GenericViewSet):
    queryset = CustomizeFormField.objects.all()
    filterset_class = CustomizeFormFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomizeFormFieldSerializer

