from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.social_login_key import SocialLoginKey
from frappe_app.filters.integrations.social_login_key import SocialLoginKeyFilter
from frappe_app.serializers.integrations.social_login_key import SocialLoginKeySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SocialLoginKeyViewSet(GenericViewSet):
    queryset = SocialLoginKey.objects.all()
    filterset_class = SocialLoginKeyFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SocialLoginKeySerializer

