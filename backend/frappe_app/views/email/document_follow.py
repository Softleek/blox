from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.email.document_follow import DocumentFollow
from frappe_app.filters.email.document_follow import DocumentFollowFilter
from frappe_app.serializers.email.document_follow import DocumentFollowSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DocumentFollowViewSet(GenericViewSet):
    queryset = DocumentFollow.objects.all()
    filterset_class = DocumentFollowFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DocumentFollowSerializer

