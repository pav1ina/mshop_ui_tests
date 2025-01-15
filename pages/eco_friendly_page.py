from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html/'

    def check_default_pagination_option(self):
        default_pagination_option = self.find(loc.pagination_option_default_loc)
        expected_quantity = int(default_pagination_option.get_attribute('innerText'))
        count_of_items = len(self.find_all(loc.cards_loc))
        assert count_of_items == expected_quantity

    def select_xs_size_and_check_items_labels(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(loc.filter_size_loc))
        select_drop_down = self.find(loc.filter_size_loc)
        select_drop_down.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(loc.xs_option_size_loc))
        select_xs_option = self.find(loc.xs_option_size_loc)
        select_xs_option.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(loc.filter_label_loc))
        selected_value = self.find(loc.filter_label_loc)
        filtered_cards = self.find_all(loc.filtered_cards_loc)
        for card in filtered_cards:
            print(card.text)
            assert card.text == 'XS'
        assert selected_value.text == 'XS'

    def clear_filter(self):
        clear_filter_button = self.find(loc.clear_filter_loc)
        clear_filter_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(loc.filter_label_loc)
        )

    def filter_price_and_check_items_price_is_in_range(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.filter_price_loc))
        select_price = self.find(loc.filter_price_loc)
        select_price.click()
        select_price_option = self.find(loc.price_option_loc)
        select_price_option.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.products_prices_loc))
        product_prices = self.find_all(loc.products_prices_loc)
        for product_price in product_prices:
            price = float(product_price.text.replace("$", ""))
            assert 10.00 <= price <= 19.99
