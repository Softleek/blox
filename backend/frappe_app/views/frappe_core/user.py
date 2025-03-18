from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.user import User
from frappe_app.filters.frappe_core.user import UserFilter
from frappe_app.serializers.frappe_core.user import UserSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    filterset_class = UserFilter
    permission_classes = [HasGroupPermission]
    serializer_class = UserSerializer

