from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.docperm import DocPerm

class DocPermSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = DocPerm
        fields = '__all__'
