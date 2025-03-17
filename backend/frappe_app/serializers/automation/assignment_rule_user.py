from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.automation.assignment_rule_user import AssignmentRuleUser

class AssignmentRuleUserSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AssignmentRuleUser
        fields = '__all__'
