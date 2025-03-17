from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_group import EmailGroup
from frappe_app.filters.email.email_group import EmailGroupFilter
from frappe_app.serializers.email.email_group import EmailGroupSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailGroupViewSet(GenericViewSet):
    queryset = EmailGroup.objects.all()
    filterset_class = EmailGroupFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailGroupSerializer

