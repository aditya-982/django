from rest_framework import serializers

class adityaAPPSerializer(serializers.Serializer):
    userName = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    number = serializers.IntegerField()
    password = serializers.CharField()
    userType = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)

class adityaLMSUpdateEmailSerliazer(serializers.Serializer):
    email = serializers.EmailField()
    number = serializers.IntegerField()
