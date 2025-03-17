from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_social_login import UserSocialLogin
from frappe_app.filters.core.user_social_login import UserSocialLoginFilter
from frappe_app.serializers.core.user_social_login import UserSocialLoginSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserSocialLoginViewSet(GenericViewSet):
    queryset = UserSocialLogin.objects.all()
    filterset_class = UserSocialLoginFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserSocialLoginSerializer

