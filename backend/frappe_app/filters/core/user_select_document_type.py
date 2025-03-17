import django_filters as filters
from frappe_app.models.core.user_select_document_type import UserSelectDocumentType

class UserSelectDocumentTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserSelectDocumentType
        fields = ['id']

