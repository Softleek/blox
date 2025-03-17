from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_theme import WebsiteTheme

class WebsiteThemeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteTheme
        fields = '__all__'
