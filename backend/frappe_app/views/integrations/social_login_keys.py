from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.social_login_keys import SocialLoginKeys
from frappe_app.filters.integrations.social_login_keys import SocialLoginKeysFilter
from frappe_app.serializers.integrations.social_login_keys import SocialLoginKeysSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SocialLoginKeysViewSet(GenericViewSet):
    queryset = SocialLoginKeys.objects.all()
    filterset_class = SocialLoginKeysFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SocialLoginKeysSerializer

