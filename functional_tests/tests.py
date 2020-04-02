from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
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
        self.wait_for_row_in_list_table('1: kill all humans')

        #There is still a text box inviting him to add another item
        #He enters "kill the rats as well"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('kill the rats as well')
        inputbox.send_keys(Keys.ENTER)

        #the page updates again and shows both items on the list
        self.wait_for_row_in_list_table('1: kill all humans')
        self.wait_for_row_in_list_table('2: kill the rats as well')

        #Satisfied he makes some noppers

    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Loki starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('kill all humans')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: kill all humans')

        #He sees that he has a unique URL 
        loki_list_url = self.browser.current_url
        self.assertRegex(loki_list_url,'lists.+')

        #Now a new user, Bbanggu, comes to the site.

        ##We use a new browser session to make sure that no information
        ##of Loki's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Bbanggu visits the homepage. There is no sign of Loki's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('kill all humans',page_text)
        self.assertNotIn('kill the rats as well',page_text)

        #Bbanggu starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('beg for food')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: beg for food')

        #Again, there is no trace of Loki's list
        page_text = self.browser.find_elements_by_tag_name('body').text
        self.assertNotIn('kill all humans',page_text)
        self.In('beg for food',page_text)

        #satisfied he makes some noppers too
