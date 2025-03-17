from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_group import EmailGroup

class EmailGroupSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailGroup
        fields = '__all__'
