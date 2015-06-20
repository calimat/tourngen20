from unittest import skip
from django.core.urlresolvers import resolve
from django.test import TestCase
from tournaments.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from tournaments.models import Team


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['team_name'] = 'Team 1'

        response = home_page(request)

        self.assertEqual(Team.objects.count(), 1)
        new_team = Team.objects.first()
        self.assertEqual(new_team.name, 'Team 1')

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['team_name'] = 'Team 1'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/tournaments/the-only-tournament-in-the-world')

    def test_home_page_only_saves_teams_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Team.objects.count(), 0)



class TeamTest(TestCase):
    def test_saving_and_retrieving_teams(self):
        first_team = Team()
        first_team.name = 'Team 1'
        first_team.save()

        second_team = Team()
        second_team.name = 'Team 2'
        second_team.save()

        saved_teams = Team.objects.all()
        self.assertEqual(saved_teams.count(), 2)

        first_saved_team = saved_teams[0]
        second_saved_team = saved_teams[1]

        self.assertEqual(first_saved_team.name, 'Team 1')
        self.assertEqual(second_saved_team.name, 'Team 2')

class TournamentViewTest(TestCase):

    def test_uses_tournament_template(self):
        response = self.client.get('/tournaments/the-only-tournament-in-the-world/')
        self.assertTemplateUsed(response, 'tournament.html')

    def test_displays_all_teams(self):
        Team.objects.create(name='teamey 1')
        Team.objects.create(name='teamey 2')


        response = self.client.get('/tournaments/the-only-tournament-in-the-world/')

        self.assertContains(response, 'teamey 1')
        self.assertContains(response, 'teamey 2')
