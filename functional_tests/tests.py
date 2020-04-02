from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_later(self):
        #Loki checks out a new app at its homepage
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: kill all humans')

        #There is still a text box inviting him to add another item
        #He enters "kill the rats as well"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('kill the rats as well')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #the page updates again and shows both items on the list
        self.check_for_row_in_list_table('1: kill all humans')
        self.check_for_row_in_list_table('2: kill the rats as well')

        #Loki hopes the site will remeber this for him because his thinker
        #is not too good. He sees that he has a unique URL and there is some
        #text to that effect as well
        self.fail('Finish the test!')

        #He visits the URL and his list is still there

        #Satisfied he makes some noppers
