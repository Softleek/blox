from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.website_theme_ignore_app import WebsiteThemeIgnoreApp

class WebsiteThemeIgnoreAppSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebsiteThemeIgnoreApp
        fields = '__all__'
