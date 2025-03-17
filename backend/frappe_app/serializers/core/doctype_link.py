from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.doctype_link import DocTypeLink

class DocTypeLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocTypeLink
        fields = '__all__'
