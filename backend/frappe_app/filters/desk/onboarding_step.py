import django_filters as filters
from frappe_app.models.desk.onboarding_step import OnboardingStep

class OnboardingStepFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OnboardingStep
        fields = ['id']

