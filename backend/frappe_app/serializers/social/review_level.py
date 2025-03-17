from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.social.review_level import ReviewLevel

class ReviewLevelSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ReviewLevel
        fields = '__all__'
