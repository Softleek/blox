from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.package_import import PackageImport

class PackageImportSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PackageImport
        fields = '__all__'
