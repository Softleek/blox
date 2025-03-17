from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.newsletter_email_group import NewsletterEmailGroup

class NewsletterEmailGroupSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NewsletterEmailGroup
        fields = '__all__'
