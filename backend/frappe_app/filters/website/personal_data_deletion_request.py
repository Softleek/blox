import django_filters as filters
from frappe_app.models.website.personal_data_deletion_request import PersonalDataDeletionRequest

class PersonalDataDeletionRequestFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PersonalDataDeletionRequest
        fields = ['id']

