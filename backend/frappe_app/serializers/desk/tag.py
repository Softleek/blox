from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.tag import Tag

class TagSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
