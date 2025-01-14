from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import sales_locators as loc


class SalesPage(BasePage):
    page_url = '/sale.html'

    def check_women_hoodies_title_and_breadcrumbs(self):
        hoodies_women_link = self.find(loc.hoodies_link_loc)
        hoodies_women_link.click()
        hoodies_page_title = self.find(loc.hoodies_title_loc)
        assert hoodies_page_title.text == 'Hoodies & Sweatshirts'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.hoodies_breadcrumbs_loc))
        breadcrumbs_elements = self.find_all(loc.hoodies_breadcrumbs_loc)
        breadcrumbs_texts = [element.text for element in breadcrumbs_elements]
        print(breadcrumbs_texts)
        expected_breadcrumbs = ['Home Women Tops Hoodies & Sweatshirts']
        assert breadcrumbs_texts == expected_breadcrumbs, "Breadcrumbs do not match expected order"

    def search_items(self, text):
        search_field = self.find(loc.search_field_loc)
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.page_title_after_search_loc))
        result_span = self.find(loc.page_title_after_search_loc)
        result_text = result_span.text
        return result_text

    def verify_error_text(self, error_text_expected):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.error_loc))
        error = self.find(loc.error_loc)
        error_text_full = error.text
        error_text_target = error_text_full.split('\n')[0].strip()
        print(error_text_target)
        assert error_text_target == error_text_expected
