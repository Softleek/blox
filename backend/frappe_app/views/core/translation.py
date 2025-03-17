from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.translation import Translation
from frappe_app.filters.core.translation import TranslationFilter
from frappe_app.serializers.core.translation import TranslationSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class TranslationViewSet(GenericViewSet):
    queryset = Translation.objects.all()
    filterset_class = TranslationFilter
    permission_classes = [HasGroupPermission]
    serializer_class = TranslationSerializer

