from unittest import skip
from django.test import TestCase

from tournaments.forms import TeamForm, EMPTY_TEAM_ERROR


class TeamFormTest(TestCase):

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