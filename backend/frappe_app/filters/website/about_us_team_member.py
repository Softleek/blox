import django_filters as filters
from frappe_app.models.website.about_us_team_member import AboutUsTeamMember

class AboutUsTeamMemberFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AboutUsTeamMember
        fields = ['id']

