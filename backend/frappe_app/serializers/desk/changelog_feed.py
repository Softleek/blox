from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.changelog_feed import ChangelogFeed

class ChangelogFeedSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ChangelogFeed
        fields = '__all__'
