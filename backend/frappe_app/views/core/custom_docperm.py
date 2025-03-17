from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.custom_docperm import CustomDocPerm
from frappe_app.filters.core.custom_docperm import CustomDocPermFilter
from frappe_app.serializers.core.custom_docperm import CustomDocPermSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CustomDocPermViewSet(GenericViewSet):
    queryset = CustomDocPerm.objects.all()
    filterset_class = CustomDocPermFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CustomDocPermSerializer

