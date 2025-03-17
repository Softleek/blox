from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.blog_category import BlogCategory
from frappe_app.filters.website.blog_category import BlogCategoryFilter
from frappe_app.serializers.website.blog_category import BlogCategorySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BlogCategoryViewSet(GenericViewSet):
    queryset = BlogCategory.objects.all()
    filterset_class = BlogCategoryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BlogCategorySerializer

