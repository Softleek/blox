from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.email_group_member import EmailGroupMember
from frappe_app.filters.email.email_group_member import EmailGroupMemberFilter
from frappe_app.serializers.email.email_group_member import EmailGroupMemberSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class EmailGroupMemberViewSet(GenericViewSet):
    queryset = EmailGroupMember.objects.all()
    filterset_class = EmailGroupMemberFilter
    permission_classes = [HasGroupPermission]
    serializer_class = EmailGroupMemberSerializer

