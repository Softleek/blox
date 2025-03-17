from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.form_tour import FormTour

class FormTourSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = FormTour
        fields = '__all__'
