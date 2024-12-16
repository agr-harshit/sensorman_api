from .models import SensorReading
from rest_framework import serializers

class SensorReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = '__all__'

class SensorNasReadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = ('id', 'nas_to_gost_manipulation1', 'nas_to_gost_manipulation2', 'nas_to_gost_manipulation3', 'nas_to_gost_manipulation4')
   