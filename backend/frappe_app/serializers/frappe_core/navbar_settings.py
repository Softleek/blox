from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.navbar_settings import NavbarSettings

class NavbarSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NavbarSettings
        fields = '__all__'
