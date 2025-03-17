import django_filters as filters
from frappe_app.models.core.deleted_document import DeletedDocument

class DeletedDocumentFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DeletedDocument
        fields = ['id']

