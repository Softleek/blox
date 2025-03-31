from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.contacts.gender import Gender
from frappe_app.filters.contacts.gender import GenderFilter
from frappe_app.serializers.contacts.gender import GenderSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class GenderViewSet(GenericViewSet):
    queryset = Gender.objects.all()
    filterset_class = GenderFilter
    permission_classes = [HasGroupPermission]
    serializer_class = GenderSerializer

    filterset_class = GenderFilter
