from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.geo.currency import Currency
from frappe_app.filters.geo.currency import CurrencyFilter
from frappe_app.serializers.geo.currency import CurrencySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CurrencyViewSet(GenericViewSet):
    queryset = Currency.objects.all()
    filterset_class = CurrencyFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CurrencySerializer

