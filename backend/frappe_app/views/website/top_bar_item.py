from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.top_bar_item import TopBarItem
from frappe_app.filters.website.top_bar_item import TopBarItemFilter
from frappe_app.serializers.website.top_bar_item import TopBarItemSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TopBarItemViewSet(GenericViewSet):
    queryset = TopBarItem.objects.all()
    filterset_class = TopBarItemFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TopBarItemSerializer

