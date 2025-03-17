from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.about_us_team_member import AboutUsTeamMember
from frappe_app.filters.website.about_us_team_member import AboutUsTeamMemberFilter
from frappe_app.serializers.website.about_us_team_member import AboutUsTeamMemberSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AboutUsTeamMemberViewSet(GenericViewSet):
    queryset = AboutUsTeamMember.objects.all()
    filterset_class = AboutUsTeamMemberFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AboutUsTeamMemberSerializer

