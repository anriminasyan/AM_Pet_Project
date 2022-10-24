from selenium.webdriver.common.by import By
from BasePage import BasePage


class GooglePage(BasePage):
    """A class for Google page search

        Methods:
            go_to_url(self)
                opens 'http://google.com'

            accept_cookies_button(self)
                clicks on accept cookies

            type_in_search_box(self, text)
                text - search keyword

            click_search_button(self)
                click Google search button

            click_url(self, text)
                text - page you want to open
                click on the page
    """
    def go_to_url(self):
        self.driver.get('http://google.com')

    def accept_cookies_button(self):
        self.click_element('L2AGLb',
                           find_by=By.ID
                           )

    def type_in_search_field(self, text):
        self.typing_text('q', text)

    def click_search_button(self):
        self.click_element('div[class="FPdoLc lJ9FBc"] input[name="btnK"]',
                           find_by=By.CSS_SELECTOR
                           )

    def click_url(self, url):
        self.click_element(f'[href*={url}]',
                           find_by=By.CSS_SELECTOR
                           )
