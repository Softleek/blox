from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.log_setting_user import LogSettingUser
from frappe_app.filters.frappe_core.log_setting_user import LogSettingUserFilter
from frappe_app.serializers.frappe_core.log_setting_user import LogSettingUserSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LogSettingUserViewSet(GenericViewSet):
    queryset = LogSettingUser.objects.all()
    filterset_class = LogSettingUserFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LogSettingUserSerializer

