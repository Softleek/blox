from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.custom_field import CustomField
from frappe_app.filters.custom.custom_field import CustomFieldFilter
from frappe_app.serializers.custom.custom_field import CustomFieldSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomFieldViewSet(GenericViewSet):
    queryset = CustomField.objects.all()
    filterset_class = CustomFieldFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomFieldSerializer

