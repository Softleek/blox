from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_template import EmailTemplate

class EmailTemplateSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailTemplate
        fields = '__all__'
