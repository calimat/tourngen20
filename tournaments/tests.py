from django.core.urlresolvers import resolve
from django.test import  TestCase
from tournaments.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from tournaments.models import Tournament

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
        request.POST['tournament_name'] = 'Tournament 1'

        response = home_page(request)

        self.assertIn('Tournament 1', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_tournament_name': 'Tournament 1'}
        )
        self.assertEqual(response.content.decode(), expected_html)

class TournamentModelTest(TestCase):

    def test_saving_and_retrieving_tournaments(self):
        tournament_item = Tournament()
        tournament_item.name = 'Tournament 1'
        tournament_item.save()


        saved_tournaments = Tournament.objects.all()
        self.assertEqual(saved_tournaments.count(), 1)

        saved_tournament = saved_tournaments[0]

        self.assertEqual(saved_tournament.name, 'Tournament 1')
