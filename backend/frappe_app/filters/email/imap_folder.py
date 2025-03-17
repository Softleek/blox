import django_filters as filters
from frappe_app.models.email.imap_folder import IMAPFolder

class IMAPFolderFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = IMAPFolder
        fields = ['id']

