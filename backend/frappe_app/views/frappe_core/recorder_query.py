from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.recorder_query import RecorderQuery
from frappe_app.filters.frappe_core.recorder_query import RecorderQueryFilter
from frappe_app.serializers.frappe_core.recorder_query import RecorderQuerySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RecorderQueryViewSet(GenericViewSet):
    queryset = RecorderQuery.objects.all()
    filterset_class = RecorderQueryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RecorderQuerySerializer

    filterset_class = RecorderQueryFilter
