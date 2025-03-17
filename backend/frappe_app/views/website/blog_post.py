from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.blog_post import BlogPost
from frappe_app.filters.website.blog_post import BlogPostFilter
from frappe_app.serializers.website.blog_post import BlogPostSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BlogPostViewSet(GenericViewSet):
    queryset = BlogPost.objects.all()
    filterset_class = BlogPostFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BlogPostSerializer

