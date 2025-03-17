from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_group_member import EmailGroupMember

class EmailGroupMemberSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailGroupMember
        fields = '__all__'
