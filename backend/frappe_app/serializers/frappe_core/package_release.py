from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.package_release import PackageRelease

class PackageReleaseSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PackageRelease
        fields = '__all__'
