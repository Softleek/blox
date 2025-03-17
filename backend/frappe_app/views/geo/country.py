from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.geo.country import Country
from frappe_app.filters.geo.country import CountryFilter
from frappe_app.serializers.geo.country import CountrySerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class CountryViewSet(GenericViewSet):
    queryset = Country.objects.all()
    filterset_class = CountryFilter
    permission_classes = [HasGroupPermission]
    serializer_class = CountrySerializer

