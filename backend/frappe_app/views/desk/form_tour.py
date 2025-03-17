from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.form_tour import FormTour
from frappe_app.filters.desk.form_tour import FormTourFilter
from frappe_app.serializers.desk.form_tour import FormTourSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class FormTourViewSet(GenericViewSet):
    queryset = FormTour.objects.all()
    filterset_class = FormTourFilter
    permission_classes = [HasGroupPermission]
    serializer_class = FormTourSerializer

