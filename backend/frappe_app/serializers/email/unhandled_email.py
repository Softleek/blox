from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.unhandled_email import UnhandledEmail

class UnhandledEmailSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = UnhandledEmail
        fields = '__all__'
