import django_filters as filters
from frappe_app.models.desk.form_tour import FormTour

class FormTourFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = FormTour
        fields = ['id']

