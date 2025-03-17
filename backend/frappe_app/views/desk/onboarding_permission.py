from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.desk.onboarding_permission import OnboardingPermission
from frappe_app.filters.desk.onboarding_permission import OnboardingPermissionFilter
from frappe_app.serializers.desk.onboarding_permission import OnboardingPermissionSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class OnboardingPermissionViewSet(GenericViewSet):
    queryset = OnboardingPermission.objects.all()
    filterset_class = OnboardingPermissionFilter
    permission_classes = [HasGroupPermission]
    serializer_class = OnboardingPermissionSerializer

