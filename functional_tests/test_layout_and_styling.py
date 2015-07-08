from selenium import webdriver
import unittest
from unittest import skip
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        #She notices the input box is nicely centered
        team_name_inputbox = self.get_team_input_box()
        self.assertAlmostEqual(
            team_name_inputbox.location['x'] + team_name_inputbox.size['width'] / 2,
            512,
            delta=5
        )
