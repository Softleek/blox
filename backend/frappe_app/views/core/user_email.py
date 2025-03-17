from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.user_email import UserEmail
from frappe_app.filters.core.user_email import UserEmailFilter
from frappe_app.serializers.core.user_email import UserEmailSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserEmailViewSet(GenericViewSet):
    queryset = UserEmail.objects.all()
    filterset_class = UserEmailFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserEmailSerializer

