from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """A class that represents web-driver actions
        initializing webdriver instance
        maximizing browser window
    """

    """Methods:
        click_element(self, selector, find_by)
            selector - selector name
            find_byt - selector type(default is By.NAME)

        typing_text(self, selector, text, find_by)
            selector - selector name
            text - accepts text as argument
            find_byt - selector type(default is By.NAME)

        get_text(self, selector, find_by)
            selector - selector name
            find_byt - selector type(default is By.NAME)
            returns InnerText of element
    """
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
        self.driver.maximize_window()

    def click_element(self, selector, find_by=By.NAME):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((find_by, selector))).click()

    def typing_text(self, selector, text, find_by=By.NAME):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((find_by, selector))).send_keys(text)

    def get_text(self, selector, find_by=By.NAME):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((find_by, selector)))
        return element.text
