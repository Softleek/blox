from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.installed_application import InstalledApplication

class InstalledApplicationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = InstalledApplication
        fields = '__all__'
