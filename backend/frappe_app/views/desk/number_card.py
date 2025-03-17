from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.number_card import NumberCard
from frappe_app.filters.desk.number_card import NumberCardFilter
from frappe_app.serializers.desk.number_card import NumberCardSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NumberCardViewSet(GenericViewSet):
    queryset = NumberCard.objects.all()
    filterset_class = NumberCardFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NumberCardSerializer

