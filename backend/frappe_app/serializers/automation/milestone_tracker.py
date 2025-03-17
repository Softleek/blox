from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.milestone_tracker import MilestoneTracker

class MilestoneTrackerSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = MilestoneTracker
        fields = '__all__'
