from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=user
		fields='__all__'
class ActivitySerializer(serializers.ModelSerializer):
	user=UserSerializer(read_only=True)
	class Meta:
		model=Activity
		fields=['start_time','end_time','user']