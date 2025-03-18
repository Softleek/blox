from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.comment import Comment

class CommentSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
