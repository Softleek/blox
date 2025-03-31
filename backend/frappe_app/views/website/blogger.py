from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.blogger import Blogger
from frappe_app.filters.website.blogger import BloggerFilter
from frappe_app.serializers.website.blogger import BloggerSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class BloggerViewSet(GenericViewSet):
    queryset = Blogger.objects.all()
    filterset_class = BloggerFilter
    permission_classes = [HasGroupPermission]
    serializer_class = BloggerSerializer

    filterset_class = BloggerFilter
