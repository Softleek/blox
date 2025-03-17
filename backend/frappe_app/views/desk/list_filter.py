from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.list_filter import ListFilter
from frappe_app.filters.desk.list_filter import ListFilterFilter
from frappe_app.serializers.desk.list_filter import ListFilterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ListFilterViewSet(GenericViewSet):
    queryset = ListFilter.objects.all()
    filterset_class = ListFilterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ListFilterSerializer

