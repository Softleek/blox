import django_filters as filters
from frappe_app.models.email.document_follow import DocumentFollow

class DocumentFollowFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocumentFollow
        fields = ['id']

