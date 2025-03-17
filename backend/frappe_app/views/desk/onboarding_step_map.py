from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.onboarding_step_map import OnboardingStepMap
from frappe_app.filters.desk.onboarding_step_map import OnboardingStepMapFilter
from frappe_app.serializers.desk.onboarding_step_map import OnboardingStepMapSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OnboardingStepMapViewSet(GenericViewSet):
    queryset = OnboardingStepMap.objects.all()
    filterset_class = OnboardingStepMapFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OnboardingStepMapSerializer

