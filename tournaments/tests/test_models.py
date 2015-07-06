from django.test import TestCase
from tournaments.models import Team, Tournament

class TeamAndTournamenTModelTest(TestCase):
    def test_saving_and_retrieving_teams(self):
        tournament_ = Tournament()
        tournament_.save()

        first_team = Team()
        first_team.name = 'Team 1'
        first_team.tournament = tournament_
        first_team.save()

        second_team = Team()
        second_team.name = 'Team 2'
        second_team.tournament = tournament_
        second_team.save()

        saved_tournament = Tournament.objects.first()
        self.assertEqual(saved_tournament, tournament_)

        saved_teams = Team.objects.all()
        self.assertEqual(saved_teams.count(), 2)

        first_saved_team = saved_teams[0]
        second_saved_team = saved_teams[1]
        self.assertEqual(first_saved_team.name, 'Team 1')
        self.assertEqual(first_saved_team.tournament, tournament_)
        self.assertEqual(second_saved_team.name, 'Team 2')
        self.assertEqual(second_saved_team.tournament, tournament_)

