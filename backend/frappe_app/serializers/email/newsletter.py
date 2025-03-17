from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.newsletter import Newsletter

class NewsletterSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'
