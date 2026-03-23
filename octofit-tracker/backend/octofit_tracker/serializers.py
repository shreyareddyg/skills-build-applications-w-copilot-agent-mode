from rest_framework import serializers
from .models import User, Team, Activity, LeaderboardEntry, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'date']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'score']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']
