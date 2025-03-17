from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.document_naming_rule_condition import DocumentNamingRuleCondition

class DocumentNamingRuleConditionSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocumentNamingRuleCondition
        fields = '__all__'
