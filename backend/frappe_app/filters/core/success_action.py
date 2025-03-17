import django_filters as filters
from frappe_app.models.core.success_action import SuccessAction

class SuccessActionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = SuccessAction
        fields = ['id']

