from rest_framework import serializers
class PredictorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
