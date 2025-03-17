from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.milestone import Milestone

class MilestoneSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = '__all__'
