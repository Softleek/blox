from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.doctype_action import DocTypeAction
from frappe_app.filters.core.doctype_action import DocTypeActionFilter
from frappe_app.serializers.core.doctype_action import DocTypeActionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocTypeActionViewSet(GenericViewSet):
    queryset = DocTypeAction.objects.all()
    filterset_class = DocTypeActionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocTypeActionSerializer

