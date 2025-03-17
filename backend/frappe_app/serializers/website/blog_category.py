from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.blog_category import BlogCategory

class BlogCategorySerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = BlogCategory
        fields = '__all__'
