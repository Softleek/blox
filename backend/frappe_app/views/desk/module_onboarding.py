from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.module_onboarding import ModuleOnboarding
from frappe_app.filters.desk.module_onboarding import ModuleOnboardingFilter
from frappe_app.serializers.desk.module_onboarding import ModuleOnboardingSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ModuleOnboardingViewSet(GenericViewSet):
    queryset = ModuleOnboarding.objects.all()
    filterset_class = ModuleOnboardingFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ModuleOnboardingSerializer

