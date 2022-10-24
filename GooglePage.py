from selenium.webdriver.common.by import By
from BasePage import BasePage


class GooglePage(BasePage):
    """A class for Google page search"""
    def go_to_url(self):
        """Method that goes to http://google.com"""
        self.driver.get('http://google.com')

    def accept_cookies_button(self):
        """Method that accepts cookies"""
        self.click_element('L2AGLb',
                           find_by=By.ID
                           )

    def type_in_search_field(self, text):
        """Method that inserts text in search field
        @:param text - value for searching
        """
        self.typing_text('q', text)

    def click_search_button(self):
        """Method that clicks on search button"""
        self.click_element('div[class="FPdoLc lJ9FBc"] input[name="btnK"]',
                           find_by=By.CSS_SELECTOR
                           )

    def click_url(self, url):
        """Method that clicks on specific url
        @:param url - specifying url
        """
        self.click_element(f'[href*={url}]',
                           find_by=By.CSS_SELECTOR
                           )
