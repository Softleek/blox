from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.about_us_settings import AboutUsSettings

class AboutUsSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AboutUsSettings
        fields = '__all__'
