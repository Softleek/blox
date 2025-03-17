from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.tag_link import TagLink
from frappe_app.filters.desk.tag_link import TagLinkFilter
from frappe_app.serializers.desk.tag_link import TagLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TagLinkViewSet(GenericViewSet):
    queryset = TagLink.objects.all()
    filterset_class = TagLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TagLinkSerializer

