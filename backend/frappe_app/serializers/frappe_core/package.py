from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.package import Package

class PackageSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'
