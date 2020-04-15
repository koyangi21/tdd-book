from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
 
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


        #And he can correct it bu filling some text in
        self.get_item_input_box().send_keys('Eat fishies')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy tooter')
        self.wait_for_row_in_list_table('2: Eat fishies')
