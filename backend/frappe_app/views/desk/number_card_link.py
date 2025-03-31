from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.desk.number_card_link import NumberCardLink
from frappe_app.filters.desk.number_card_link import NumberCardLinkFilter
from frappe_app.serializers.desk.number_card_link import NumberCardLinkSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NumberCardLinkViewSet(GenericViewSet):
    queryset = NumberCardLink.objects.all()
    filterset_class = NumberCardLinkFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NumberCardLinkSerializer

    filterset_class = NumberCardLinkFilter
