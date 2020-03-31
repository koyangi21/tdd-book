from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        #Loki checks out a new app at its homepage
        self.browser.get('http://localhost:8000')

        #He notices the title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')

        #He is invited to enter a to-do item straight away

        #He types in "kill all humans" into a text box

        #When he hits enter page updates and lists "1: kill all humans" as an
        #item in a to-do list

        #There is still a text box inviting him to add another item
        #He enters "kill the rats as well"

        #the page updates again and shows both items on the list

        #Loki hopes the site will remeber this for him because his thinker
        #is not too good. He sees that he has a unique URL and there is some
        #text to that effect as well

        #He visits the URL and his list is still there

        #Satisfied he makes some noppers

if __name__=='__main__':
    unittest.main(warnings='ignore')
