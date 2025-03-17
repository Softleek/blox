from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.docshare import DocShare

class DocShareSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocShare
        fields = '__all__'
