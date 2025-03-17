from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.user_email import UserEmail

class UserEmailSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UserEmail
        fields = '__all__'
