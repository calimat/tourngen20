from unittest import skip
from django.core.urlresolvers import resolve
from django.test import TestCase
from tournaments.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from tournaments.models import Team, Tournament
from django.utils.html import escape
from tournaments.forms import TeamForm

class HomePageTest(TestCase):
    maxDiff = None

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', {'form': TeamForm()})
        self.assertMultiLineEqual(response.content.decode(), expected_html)

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html') #1

    def test_home_page_uses_team_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], TeamForm) #2


class NewTournamentTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/tournaments/new',
            data={'name': 'Team 1'}
        )

        self.assertEqual(Team.objects.count(), 1)
        new_team = Team.objects.first()
        self.assertEqual(new_team.name, 'Team 1')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/tournaments/new',
            data={'name': 'Team 1'}
        )
        new_tournament = Tournament.objects.first()
        self.assertRedirects(response, '/tournaments/%d/' % (new_tournament.id,))

    def test_passes_correct_tournament_to_template(self):
        other_tournament = Tournament.objects.create()
        correct_tournament = Tournament.objects.create()
        response = self.client.get('/tournaments/%d/' % (correct_tournament.id,))
        self.assertEqual(response.context['tournament'], correct_tournament)

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/tournaments/new', data={'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("Please enter a name for your team")
        self.assertContains(response, expected_error)

    def test_invalid_tournament_teams_arent_saved(self):
        self.client.post('/tournaments/new', data={'name': ''})
        self.assertEqual(Tournament.objects.count(), 0)
        self.assertEqual(Team.objects.count(), 0)


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

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_tournament = Tournament.objects.create()
        correct_tournament = Tournament.objects.create()

        self.client.post(
            '/tournaments/%d/' % (correct_tournament.id,),
            data={'name': 'A new team for an existing tournament'}
        )

        self.assertEqual(Team.objects.count(), 1)
        new_team = Team.objects.first()
        self.assertEqual(new_team.name, 'A new team for an existing tournament')
        self.assertEqual(new_team.tournament, correct_tournament)

    def test_POST_redirects_to_tournament_view(self):
        other_tournament = Tournament.objects.create()
        correct_tournament = Tournament.objects.create()

        response = self.client.post(
            '/tournaments/%d/' % (correct_tournament.id,),
            data={'name': 'A new team for an existing tournament'}
        )

        self.assertRedirects(response, '/tournaments/%d/' % (correct_tournament.id,))

    def test_validation_errors_end_up_on_tournaments_page(self):
        tournament = Tournament.objects.create()
        response = self.client.post(
            '/tournaments/%d/' % (tournament.id,),
            data={'name': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tournament.html')
        expected_error = escape("Please enter a name for your team")
        self.assertContains(response, expected_error)