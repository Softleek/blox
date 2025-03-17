import django_filters as filters
from frappe_app.models.core.user_email import UserEmail

class UserEmailFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserEmail
        fields = ['id']

