from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.discussion_reply import DiscussionReply
from frappe_app.filters.website.discussion_reply import DiscussionReplyFilter
from frappe_app.serializers.website.discussion_reply import DiscussionReplySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DiscussionReplyViewSet(GenericViewSet):
    queryset = DiscussionReply.objects.all()
    filterset_class = DiscussionReplyFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DiscussionReplySerializer

