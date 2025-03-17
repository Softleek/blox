from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.tag import Tag
from frappe_app.filters.desk.tag import TagFilter
from frappe_app.serializers.desk.tag import TagSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TagViewSet(GenericViewSet):
    queryset = Tag.objects.all()
    filterset_class = TagFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TagSerializer

