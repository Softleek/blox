from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_settings import WebsiteSettings

class WebsiteSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteSettings
        fields = '__all__'
