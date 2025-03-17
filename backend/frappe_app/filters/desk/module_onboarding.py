import django_filters as filters
from frappe_app.models.desk.module_onboarding import ModuleOnboarding

class ModuleOnboardingFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ModuleOnboarding
        fields = ['id']

