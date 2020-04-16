from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')
 
    def test_cannot_add_empty_list_items(self):
        #Loki goes to the home page and accidentally tries to submit
        #an empty list item. He hits Enter on the empty text box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        #The browser intercepts the request, and does not load the 
        #list page
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:invalid'
        ))

        #He types some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy tooter')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid'
        ))

        #Now he can see it correctly
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy tooter')

        #Being a rebel, he tries to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        #Again the browser will not comply
        self.wait_for_row_in_list_table('1: Buy tooter')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:invalid'
        ))


        #And he can correct it by filling some text in
        self.get_item_input_box().send_keys('Eat fishies')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy tooter')
        self.wait_for_row_in_list_table('2: Eat fishies')

    def test_cannot_add_duplicate_items(self):
        #Loki goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Kill the ribbon')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Kill the ribbon')

        #He accidently enters a duplicate item
        self.get_item_input_box().send_keys('Kill the ribbon')
        self.get_item_input_box().send_keys(Keys.ENTER)

        #He sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        #Loki starts a list and causes a validation error
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Sit on mommy')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Sit on mommy')
        self.get_item_input_box().send_keys('Sit on mommy')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        #He starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        #He is pleased to see the error message disappears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
