from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.discussion_topic import DiscussionTopic

class DiscussionTopicSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DiscussionTopic
        fields = '__all__'
