import django_filters as filters
from frappe_app.models.email.unhandled_email import UnhandledEmail

class UnhandledEmailFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UnhandledEmail
        fields = ['id']

