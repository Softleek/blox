import django_filters as filters
from frappe_app.models.website.personal_data_deletion_step import PersonalDataDeletionStep

class PersonalDataDeletionStepFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PersonalDataDeletionStep
        fields = ['id']

