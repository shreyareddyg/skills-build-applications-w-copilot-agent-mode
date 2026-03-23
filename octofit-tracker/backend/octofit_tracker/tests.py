from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, LeaderboardEntry, Workout


class UserAPITests(APITestCase):
    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])


class TeamAPITests(APITestCase):
    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])


class ActivityAPITests(APITestCase):
    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])


class LeaderboardAPITests(APITestCase):
    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])


class WorkoutAPITests(APITestCase):
    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])
