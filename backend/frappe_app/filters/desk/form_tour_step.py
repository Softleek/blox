import django_filters as filters
from frappe_app.models.desk.form_tour_step import FormTourStep

class FormTourStepFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = FormTourStep
        fields = ['id']

