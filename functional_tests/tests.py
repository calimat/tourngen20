from selenium import webdriver
import unittest
from unittest import skip
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_team_table(self, row_text):
        team_table = self.browser.find_element_by_id('id_team_table')
        rows = team_table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_enter_a_team_and_retrieve_it_later(self):
        #User enters the new tournament generator app
        self.browser.get(self.live_server_url)

        #She notices the page title and header "TOURNGEN"
        self.assertIn('Tourngen', self.browser.title)


        #She sees a label for the tournament name input box that says Name
        #tournament_name_label = self.browser.find_element_by_id('id_tournament_name_label')
        #self.assertIn('Name', tournament_name_label)

        # She is invited to insert the name of the tournament   with  a label that says name
        team_form = self.browser.find_element_by_id('id_team_form')
        team_name_label = self.browser.find_element_by_id('id_team_name_label')

        self.assertEqual(team_name_label.text, "Name:")
        team_name_inputbox = self.browser.find_element_by_id('id_team_name')



        #She types "Tournament 1" in the name of the tournament  
        team_name_inputbox.send_keys('Team 1')



        #tournament_name_inputbox.send_keys(Keys.ENTER)
        # When she hits enter, she is taken to a new URL,
        # and now the page lists "Team 1" as an item in a
        # teams table
        save_button = self.browser.find_element_by_id('id_team_save')
        save_button.click()
        edith_tournament_url = self.browser.current_url
        self.assertRegex(edith_tournament_url, '/tournaments/.+')
        self.check_for_row_in_team_table('Team 1')

        #There still a form to fill out to add another team. She enters Team 2
        team_name_inputbox = self.browser.find_element_by_id('id_team_name')
        team_name_inputbox.send_keys('Team 2')
        save_button = self.browser.find_element_by_id('id_team_save')
        save_button.click()

        #The page updates again and shows both teams
        self.check_for_row_in_team_table('Team 1')
        self.check_for_row_in_team_table('Team 2')

        #Now a new user, Francis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There's no sign of Edith's
        # tournament
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Team 1', page_text)
        self.assertNotIn('Team 2', page_text)

        #Francis starts a new tournament by entering a new team.
        # He has Qzar teams
        tournament_name_inputbox = self.browser.find_element_by_id('id_team_name')
        tournament_name_inputbox.send_keys('Q-Guerreros')
        save_button = self.browser.find_element_by_id('id_team_save')
        save_button.click()

        #Francis gets his own unique URL
        francis_tournament_url = self.browser.current_url
        self.assertRegex(francis_tournament_url, '/tournaments/.+')
        self.assertNotEqual(francis_tournament_url, edith_tournament_url)

        #Again, there is no trace of Edith's tournament
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Team 1', page_text)
        self.assertIn('Q-Guerreros', page_text)

        #Statisfied they go back to sleep

        #She types Checks the checkbox since she wants to create 
        #to create a public tournament  

        #She clicks on the calendar icon for starting date, she 
        #selects it to be today  

        #She clicks on the end date icon of the calendar 
        #selects it to be tommorrow  

        #She selects from the typ dropdown box the 
        #type of tournament as "League"  

        #She selects from the sport dropdown the 
        #sport of the tournament as Qzar  

        #She types "3" for winning score points  

        #She types "1" for tying score points  

        #She types "0" for losing score points  

        #When she finishes entering all the criteria she clicks on 
        #the save button  

        #As soon as she clicks save , the page refreshes and she looks 
        # that her tournament was created with the fields that she entered.  

        #self.fail('Finish the test')
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')

