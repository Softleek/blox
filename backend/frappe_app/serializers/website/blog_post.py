from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.blog_post import BlogPost

class BlogPostSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
