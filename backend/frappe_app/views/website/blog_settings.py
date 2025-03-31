from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.blog_settings import BlogSettings
from frappe_app.filters.website.blog_settings import BlogSettingsFilter
from frappe_app.serializers.website.blog_settings import BlogSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BlogSettingsViewSet(SingleInstanceViewSet):
    queryset = BlogSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = BlogSettingsSerializer

    filterset_class = BlogSettingsFilter
