from unittest import skip
from django.test import TestCase

from tournaments.forms import TeamForm, EMPTY_TEAM_ERROR
from tournaments.models import Tournament, Team


class TeamFormTest(TestCase):

    @skip
    def test_form(self):
        form = TeamForm()
        self.fail(form.as_p())

    def test_form_validation_for_blank_teams(self):
        form = TeamForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['name'],
            [EMPTY_TEAM_ERROR]
        )

    def test_form_team_input_has_css_classes(self):
        form = TeamForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_save_handles_saving_to_a_tournament(self):
        tournament = Tournament.objects.create()
        form = TeamForm(data={'name': 'do me'})
        new_team = form.save(tournament=tournament)
        self.assertEqual(new_team, Team.objects.first())
        self.assertEqual(new_team.name, 'do me')
        self.assertEqual(new_team.tournament, tournament)