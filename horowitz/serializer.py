from rest_framework import serializers

from horowitz.models import Symptoms, BoreliaEvents, HealthCondition


class SymptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptoms
        fields = '__all__'


class BoreliaEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoreliaEvents
        fields = '__all__'


class HealthConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCondition
        fields = '__all__'
