from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.document_naming_rule import DocumentNamingRule

class DocumentNamingRuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocumentNamingRule
        fields = '__all__'
