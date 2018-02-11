from rest_framework import serializers

from ESSArch_Core.maintenance.models import (AppraisalJob, AppraisalRule,
                                             ConversionJob, ConversionRule,
                                             MaintenanceJob, MaintenanceRule)


class MaintenanceRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRule
        fields = (
            'id', 'name', 'frequency', 'specification',
        )


class MaintenanceJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJob
        fields = (
            'id', 'rule', 'status', 'start_date', 'end_date',
        )


class AppraisalRuleSerializer(MaintenanceRuleSerializer):
    class Meta(MaintenanceRuleSerializer.Meta):
        model = AppraisalRule


class AppraisalJobSerializer(MaintenanceJobSerializer):
    class Meta(MaintenanceJobSerializer.Meta):
        model = AppraisalJob


class ConversionRuleSerializer(MaintenanceRuleSerializer):
    def validate_specification(self, value):
        """
        Ensure that the specification is not empty
        """

        if not value:
            raise serializers.ValidationError("Specification cannot be empty")
        return value
    class Meta(MaintenanceRuleSerializer.Meta):
        model = ConversionRule


class ConversionJobSerializer(MaintenanceJobSerializer):
    class Meta(MaintenanceJobSerializer.Meta):
        model = ConversionJob
