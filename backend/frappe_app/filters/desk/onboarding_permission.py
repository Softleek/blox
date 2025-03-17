import django_filters as filters
from frappe_app.models.desk.onboarding_permission import OnboardingPermission

class OnboardingPermissionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = OnboardingPermission
        fields = ['id']

