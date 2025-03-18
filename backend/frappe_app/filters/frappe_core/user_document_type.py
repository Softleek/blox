import django_filters as filters
from frappe_app.models.frappe_core.user_document_type import UserDocumentType

class UserDocumentTypeFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = UserDocumentType
        fields = ['id']

