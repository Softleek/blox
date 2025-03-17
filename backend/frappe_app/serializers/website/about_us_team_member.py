from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.about_us_team_member import AboutUsTeamMember

class AboutUsTeamMemberSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AboutUsTeamMember
        fields = '__all__'
