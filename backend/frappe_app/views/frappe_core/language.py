from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.language import Language
from frappe_app.filters.frappe_core.language import LanguageFilter
from frappe_app.serializers.frappe_core.language import LanguageSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LanguageViewSet(GenericViewSet):
    queryset = Language.objects.all()
    filterset_class = LanguageFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LanguageSerializer

    filterset_class = LanguageFilter
