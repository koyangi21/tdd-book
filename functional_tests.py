from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #He types in "kill all humans" into a text box
        inputbox.send_keys('kill all humans')

        #When he hits enter page updates and lists "1: kill all humans" as an
        #item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: kill all humans' for row in rows),
            "New to-do item did not appear in table"
        )

        #There is still a text box inviting him to add another item
        #He enters "kill the rats as well"
        self.Fail('Finish the test!') 

        #the page updates again and shows both items on the list

        #Loki hopes the site will remeber this for him because his thinker
        #is not too good. He sees that he has a unique URL and there is some
        #text to that effect as well

        #He visits the URL and his list is still there

        #Satisfied he makes some noppers

if __name__=='__main__':
    unittest.main(warnings='ignore')
