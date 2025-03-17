from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.success_action import SuccessAction
from frappe_app.filters.core.success_action import SuccessActionFilter
from frappe_app.serializers.core.success_action import SuccessActionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SuccessActionViewSet(GenericViewSet):
    queryset = SuccessAction.objects.all()
    filterset_class = SuccessActionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SuccessActionSerializer

