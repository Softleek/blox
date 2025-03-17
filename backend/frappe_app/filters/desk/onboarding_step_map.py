import django_filters as filters
from frappe_app.models.desk.onboarding_step_map import OnboardingStepMap

class OnboardingStepMapFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OnboardingStepMap
        fields = ['id']

