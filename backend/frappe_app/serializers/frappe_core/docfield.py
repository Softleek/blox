from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.docfield import DocField

class DocFieldSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocField
        fields = '__all__'
