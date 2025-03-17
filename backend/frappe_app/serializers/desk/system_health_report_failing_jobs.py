from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_health_report_failing_jobs import SystemHealthReportFailingJobs

class SystemHealthReportFailingJobsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemHealthReportFailingJobs
        fields = '__all__'
