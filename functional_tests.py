from selenium import webdriver
import unittest


class NewTournamentCreation(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_a_tournament_and_retrieve_it_later(self):
        #User enters the new tournament generator app
        self.browser.get('http://localhost:8000')

        #She notices the page title and header "TOURNGEN"
        self.assertIn('Tourngen', self.browser.title)


        #She sees a label for the tournament name input box that says Name
        #tournament_name_label = self.browser.find_element_by_id('id_tournament_name_label')
        #self.assertIn('Name', tournament_name_label)

        # She is invited to insert the name of the tournament  
        tournament_name_inputbox = self.browser.find_element_by_id('id_tournament_name')

        #She types "Tournament 1" in the name of the tournament  
        tournament_name_inputbox.send_keys('Tournament 1')

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