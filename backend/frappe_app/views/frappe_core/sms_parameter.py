from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.sms_parameter import SMSParameter
from frappe_app.filters.frappe_core.sms_parameter import SMSParameterFilter
from frappe_app.serializers.frappe_core.sms_parameter import SMSParameterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SMSParameterViewSet(GenericViewSet):
    queryset = SMSParameter.objects.all()
    filterset_class = SMSParameterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SMSParameterSerializer

