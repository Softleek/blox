import django_filters as filters
from frappe_app.models.custom.customize_form import CustomizeForm

class CustomizeFormFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = CustomizeForm
        fields = ['id']

