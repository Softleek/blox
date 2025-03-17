from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.doctype_layout_field import DocTypeLayoutField

class DocTypeLayoutFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocTypeLayoutField
        fields = '__all__'
