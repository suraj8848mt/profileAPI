from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
	''' Seriallizes a name fields for testing our APIView '''
	name = serializers.CharField(max_length=20)	