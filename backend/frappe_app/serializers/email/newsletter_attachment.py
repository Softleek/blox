from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.newsletter_attachment import NewsletterAttachment

class NewsletterAttachmentSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NewsletterAttachment
        fields = '__all__'
