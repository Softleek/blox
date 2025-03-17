import django_filters as filters
from frappe_app.models.core.document_share_key import DocumentShareKey

class DocumentShareKeyFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocumentShareKey
        fields = ['id']

