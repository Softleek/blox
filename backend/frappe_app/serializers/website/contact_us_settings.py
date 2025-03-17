from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.contact_us_settings import ContactUsSettings

class ContactUsSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ContactUsSettings
        fields = '__all__'
