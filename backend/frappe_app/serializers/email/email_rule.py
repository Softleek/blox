from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_rule import EmailRule

class EmailRuleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailRule
        fields = '__all__'
