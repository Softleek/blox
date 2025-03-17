from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.assignment_rule_day import AssignmentRuleDay

class AssignmentRuleDaySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AssignmentRuleDay
        fields = '__all__'
