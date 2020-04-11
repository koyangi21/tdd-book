from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
 
    def test_cannot_add_empty_list_items(self):
        #Loki goes to the home page and accidentally tries to submit
        #an empty list item. He hits Enter on the empty text box

        #The hompe page refreshes, and there is an error message saying
        #that list items cannot be blank

        #He tries again with some text for the item, which now works

        #Being a rebel, he tries to submit a second blank list item

        #He receives a similar warning on the list page

        #And he can correct it bu filling some text in
        self.fail('write me!')
