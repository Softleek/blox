from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.help_category import HelpCategory
from frappe_app.filters.website.help_category import HelpCategoryFilter
from frappe_app.serializers.website.help_category import HelpCategorySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class HelpCategoryViewSet(GenericViewSet):
    queryset = HelpCategory.objects.all()
    filterset_class = HelpCategoryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = HelpCategorySerializer

