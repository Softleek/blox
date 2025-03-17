from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.query_parameters import QueryParameters
from frappe_app.filters.integrations.query_parameters import QueryParametersFilter
from frappe_app.serializers.integrations.query_parameters import QueryParametersSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class QueryParametersViewSet(GenericViewSet):
    queryset = QueryParameters.objects.all()
    filterset_class = QueryParametersFilter
    permission_classes = [HasGroupPermission]
    serializer_class = QueryParametersSerializer

