from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.installed_applications import InstalledApplications

class InstalledApplicationsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = InstalledApplications
        fields = '__all__'
