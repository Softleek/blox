import django_filters as filters
from frappe_app.models.email.email_group_member import EmailGroupMember

class EmailGroupMemberFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = EmailGroupMember
        fields = ['id']

