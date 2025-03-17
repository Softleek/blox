from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.discussion_topic import DiscussionTopic
from frappe_app.filters.website.discussion_topic import DiscussionTopicFilter
from frappe_app.serializers.website.discussion_topic import DiscussionTopicSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DiscussionTopicViewSet(GenericViewSet):
    queryset = DiscussionTopic.objects.all()
    filterset_class = DiscussionTopicFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DiscussionTopicSerializer

