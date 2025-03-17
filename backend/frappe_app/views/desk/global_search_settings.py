from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.global_search_settings import GlobalSearchSettings
from frappe_app.filters.desk.global_search_settings import GlobalSearchSettingsFilter
from frappe_app.serializers.desk.global_search_settings import GlobalSearchSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GlobalSearchSettingsViewSet(GenericViewSet):
    queryset = GlobalSearchSettings.objects.all()
    filterset_class = GlobalSearchSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GlobalSearchSettingsSerializer

