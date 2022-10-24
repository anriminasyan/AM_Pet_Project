from selenium.webdriver.common.by import By


from GooglePage import GooglePage
page = GooglePage()

page.go_to_url()
page.accept_cookies_button()
page.type_in_search_field('softserve')
page.click_search_button()
page.click_url('softserveinc')
banner = page.get_text('[class*=banner__text]',
                       find_by=By.CSS_SELECTOR
                       )

assert banner == 'EXPLORE SOFTSERVE IN BULGARIA' \
       or banner == 'SOFTSERVE STANDS WITH UKRAINE'
