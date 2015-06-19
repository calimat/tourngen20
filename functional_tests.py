from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewTournamentCreation(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_tournament_table(self, row_text):
        tournnament_table = self.browser.find_element_by_id('id_tournament_table')
        rows = tournnament_table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_enter_a_tournament_and_retrieve_it_later(self):
        #User enters the new tournament generator app
        self.browser.get('http://localhost:8000')

        #She notices the page title and header "TOURNGEN"
        self.assertIn('Tourngen', self.browser.title)


        #She sees a label for the tournament name input box that says Name
        #tournament_name_label = self.browser.find_element_by_id('id_tournament_name_label')
        #self.assertIn('Name', tournament_name_label)

        # She is invited to insert the name of the tournament   with  a label that says name
        tournament_form = self.browser.find_element_by_id('id_tournament_form')
        tournament_name_label = self.browser.find_element_by_id('id_tournament_name_label')

        self.assertEqual(tournament_name_label.text, "Name:")
        tournament_name_inputbox = self.browser.find_element_by_id('id_tournament_name')



        #She types "Tournament 1" in the name of the tournament  
        tournament_name_inputbox.send_keys('Tournament 1')



        #tournament_name_inputbox.send_keys(Keys.ENTER)
        #She sees a save button and clicks on it
        save_button = self.browser.find_element_by_id('id_tournament_save')
        save_button.click()


        self.check_for_row_in_tournament_table('Tournament 1')


        #Edith decides to enter a second Tournament
        #self.assertIn('Tournament 2', [row.text for row in rows])

        #self.assertEqual(save_button.value, "Save")


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

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')