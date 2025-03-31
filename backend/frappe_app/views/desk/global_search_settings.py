from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.global_search_settings import GlobalSearchSettings
from frappe_app.filters.desk.global_search_settings import GlobalSearchSettingsFilter
from frappe_app.serializers.desk.global_search_settings import GlobalSearchSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GlobalSearchSettingsViewSet(SingleInstanceViewSet):
    queryset = GlobalSearchSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = GlobalSearchSettingsSerializer

    filterset_class = GlobalSearchSettingsFilter
