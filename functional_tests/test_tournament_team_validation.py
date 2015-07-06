from selenium import webdriver
import unittest
from unittest import skip
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from .base import FunctionalTest


class TeamValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_tournament_teams(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_team_name').send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error') #1
        self.assertEqual(error.text, "Please enter a name for your team")

        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_team_name').send_keys('Q-Guerreros\n')
        self.check_for_row_in_list_table('Q-Guerreros') #2

        # Perversely, she now decides to submit a second blank list item
        self.browser.find_element_by_id('id_team_name').send_keys('\n')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('Q-Guerreros')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Please enter a name for your team")

        # And she can correct it by filling some text in
        self.browser.find_element_by_id('id_team_name').send_keys('Q-B2\n')
        self.check_for_row_in_list_table('Q-Guerreros')
        self.check_for_row_in_list_table('Q-B2')