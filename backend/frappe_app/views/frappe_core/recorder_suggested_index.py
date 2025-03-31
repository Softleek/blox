from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.recorder_suggested_index import RecorderSuggestedIndex
from frappe_app.filters.frappe_core.recorder_suggested_index import RecorderSuggestedIndexFilter
from frappe_app.serializers.frappe_core.recorder_suggested_index import RecorderSuggestedIndexSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class RecorderSuggestedIndexViewSet(GenericViewSet):
    queryset = RecorderSuggestedIndex.objects.all()
    filterset_class = RecorderSuggestedIndexFilter
    permission_classes = [HasGroupPermission]
    serializer_class = RecorderSuggestedIndexSerializer

    filterset_class = RecorderSuggestedIndexFilter
