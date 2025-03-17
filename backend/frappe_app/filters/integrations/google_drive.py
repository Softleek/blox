import django_filters as filters
from frappe_app.models.integrations.google_drive import GoogleDrive

class GoogleDriveFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = GoogleDrive
        fields = ['id']

