from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, LeaderboardEntry, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()

        # Create users (superheroes)
        users = [
            User(name='Tony Stark', email='tony@avengers.com', password='ironman123'),
            User(name='Steve Rogers', email='steve@avengers.com', password='cap123'),
            User(name='Bruce Banner', email='bruce@avengers.com', password='hulk123'),
            User(name='Peter Parker', email='peter@marvel.com', password='spidey123'),
            User(name='Bruce Wayne', email='bruce@dc.com', password='batman123'),
            User(name='Clark Kent', email='clark@dc.com', password='superman123'),
            User(name='Diana Prince', email='diana@dc.com', password='wonder123'),
        ]
        for user in users:
            user.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))

        # Create teams
        team_marvel = Team(
            name='Team Marvel',
            members=['tony@avengers.com', 'steve@avengers.com', 'bruce@avengers.com', 'peter@marvel.com']
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['bruce@dc.com', 'clark@dc.com', 'diana@dc.com']
        )
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('Created 2 teams: Team Marvel and Team DC'))

        # Create activities
        activities = [
            Activity(user='tony@avengers.com', activity_type='Running', duration=30.0, date=date(2024, 1, 15)),
            Activity(user='steve@avengers.com', activity_type='Strength Training', duration=60.0, date=date(2024, 1, 15)),
            Activity(user='bruce@avengers.com', activity_type='Walking', duration=45.0, date=date(2024, 1, 16)),
            Activity(user='peter@marvel.com', activity_type='Running', duration=25.0, date=date(2024, 1, 16)),
            Activity(user='bruce@dc.com', activity_type='Strength Training', duration=90.0, date=date(2024, 1, 17)),
            Activity(user='clark@dc.com', activity_type='Running', duration=20.0, date=date(2024, 1, 17)),
            Activity(user='diana@dc.com', activity_type='Strength Training', duration=75.0, date=date(2024, 1, 18)),
        ]
        for activity in activities:
            activity.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(activities)} activities'))

        # Create leaderboard entries
        leaderboard_entries = [
            LeaderboardEntry(user='Steve Rogers', score=950),
            LeaderboardEntry(user='Diana Prince', score=900),
            LeaderboardEntry(user='Bruce Wayne', score=875),
            LeaderboardEntry(user='Tony Stark', score=820),
            LeaderboardEntry(user='Peter Parker', score=780),
            LeaderboardEntry(user='Clark Kent', score=750),
            LeaderboardEntry(user='Bruce Banner', score=700),
        ]
        for entry in leaderboard_entries:
            entry.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(leaderboard_entries)} leaderboard entries'))

        # Create workouts
        workouts = [
            Workout(name='Iron Man Cardio', description='High intensity running and cardio workout inspired by Tony Stark', duration=30),
            Workout(name='Captain America Strength', description='Full body strength training like Steve Rogers', duration=60),
            Workout(name='Hulk Power', description='Intense weightlifting and power training', duration=45),
            Workout(name='Spider-Man Agility', description='Agility and flexibility workout for quick movements', duration=25),
            Workout(name='Batman Combat', description='Martial arts and combat fitness training', duration=90),
            Workout(name='Superman Endurance', description='Ultra endurance training for stamina', duration=120),
            Workout(name='Wonder Woman Warrior', description='Warrior fitness combining strength and agility', duration=75),
        ]
        for workout in workouts:
            workout.save()
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workouts'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
