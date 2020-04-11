from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
 
    def test_cannot_add_empty_list_items(self):
        #Loki goes to the home page and accidentally tries to submit
        #an empty list item. He hits Enter on the empty text box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        #The home page refreshes, and there is an error message saying
        #that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You can't have an empty list item"
        ))

        #He tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy tooter')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy tooter')

        #Being a rebel, he tries to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        #He receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You can't have an empty list item"
        ))


        #And he can correct it bu filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Eat fishies')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy tooter')
        self.wait_for_row_in_list_table('2: Eat fishies')