from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.form_tour_step import FormTourStep

class FormTourStepSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = FormTourStep
        fields = '__all__'
