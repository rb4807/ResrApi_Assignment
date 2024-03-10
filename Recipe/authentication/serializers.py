from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username','password']

    def create(self,validated_data):
        new_user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        new_user.save()
        return new_user