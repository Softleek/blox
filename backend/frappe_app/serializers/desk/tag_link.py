from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.tag_link import TagLink

class TagLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = TagLink
        fields = '__all__'
