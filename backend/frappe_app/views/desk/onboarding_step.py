from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.onboarding_step import OnboardingStep
from frappe_app.filters.desk.onboarding_step import OnboardingStepFilter
from frappe_app.serializers.desk.onboarding_step import OnboardingStepSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OnboardingStepViewSet(GenericViewSet):
    queryset = OnboardingStep.objects.all()
    filterset_class = OnboardingStepFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OnboardingStepSerializer

