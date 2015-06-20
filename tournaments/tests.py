from unittest import skip
from django.core.urlresolvers import resolve
from django.test import TestCase
from tournaments.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from tournaments.models import Team, Tournament


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class NewTournamentTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/tournaments/new',
            data={'team_name': 'Team 1'}
        )

        self.assertEqual(Team.objects.count(), 1)
        new_team = Team.objects.first()
        self.assertEqual(new_team.name, 'Team 1')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/tournaments/new',
            data={'team_name': 'Team 1'}
        )
        new_tournament = Tournament.objects.first()
        self.assertRedirects(response, '/tournaments/%d/' % (new_tournament.id,))


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


class TournamentViewTest(TestCase):
    def test_uses_tournament_template(self):
        tournament = Tournament.objects.create()
        response = self.client.get('/tournaments/%d/' % (tournament.id,))
        self.assertTemplateUsed(response, 'tournament.html')

    def test_displays_only_teams_for_that_tournament(self):
        correct_tournament = Tournament.objects.create()
        Team.objects.create(name='teamey 1', tournament=correct_tournament)
        Team.objects.create(name='teamey 2', tournament=correct_tournament)
        other_tournament = Tournament.objects.create()
        Team.objects.create(name='other tournament team 1', tournament=other_tournament)
        Team.objects.create(name='other tournament team 2', tournament=other_tournament)

        response = self.client.get('/tournaments/%d/' % (correct_tournament.id,))

        self.assertContains(response, 'teamey 1')
        self.assertContains(response, 'teamey 2')
        self.assertNotContains(response, 'other tournament team 1')
        self.assertNotContains(response, 'other tournament team 2')
