from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.form_tour_step import FormTourStep
from frappe_app.filters.desk.form_tour_step import FormTourStepFilter
from frappe_app.serializers.desk.form_tour_step import FormTourStepSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class FormTourStepViewSet(GenericViewSet):
    queryset = FormTourStep.objects.all()
    filterset_class = FormTourStepFilter
    permission_classes = [HasGroupPermission]
    serializer_class = FormTourStepSerializer

