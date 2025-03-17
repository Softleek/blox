from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.assignment_rule import AssignmentRule

class AssignmentRuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AssignmentRule
        fields = '__all__'
