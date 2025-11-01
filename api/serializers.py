from rest_framework import serializers
from django.contrib.auth.models import User
from DBApp.models import Employee

class EmpSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
        