from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.discussion_reply import DiscussionReply

class DiscussionReplySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DiscussionReply
        fields = '__all__'
