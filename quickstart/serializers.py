from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import member, activity_period


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = member
        fields = ['id', 'real_name', 'tz']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = activity_period
        fields = ['start_time', 'end_time']
