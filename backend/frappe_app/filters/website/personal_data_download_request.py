import django_filters as filters
from frappe_app.models.website.personal_data_download_request import PersonalDataDownloadRequest

class PersonalDataDownloadRequestFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PersonalDataDownloadRequest
        fields = ['id']

