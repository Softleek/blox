from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.blog_settings import BlogSettings
from frappe_app.filters.website.blog_settings import BlogSettingsFilter
from frappe_app.serializers.website.blog_settings import BlogSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BlogSettingsViewSet(GenericViewSet):
    queryset = BlogSettings.objects.all()
    filterset_class = BlogSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BlogSettingsSerializer

