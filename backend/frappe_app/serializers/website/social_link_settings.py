from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.social_link_settings import SocialLinkSettings

class SocialLinkSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SocialLinkSettings
        fields = '__all__'
