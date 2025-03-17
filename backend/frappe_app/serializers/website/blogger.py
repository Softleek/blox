from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.website.blogger import Blogger

class BloggerSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Blogger
        fields = '__all__'
