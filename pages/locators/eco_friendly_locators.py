from selenium.webdriver.common.by import By


pagination_option_default_loc = (By.XPATH, '//select[@id="limiter"]/child::option[@value="12"]')
pagination_drop_down_loc = (By.XPATH, '//*[@id="limiter"]')
cards_loc = (By.XPATH, '//li[@class="item product product-item"]')
filter_size_loc = (By.XPATH, "(//div[@class='filter-options-title' and @tabindex='0'])[3]")
xs_option_size_loc = (By.XPATH, "//a[@aria-label='XS']/div")
filter_label_loc = (By.CSS_SELECTOR, '[class="filter-value"]')
clear_filter_loc = (By.CSS_SELECTOR, 'a.action.clear.filter-clear')
filtered_cards_loc = (By.XPATH,
                      '//li[@class="item product product-item"]/following::div[@class="swatch-option text selected"]')
filter_price_loc = (By.XPATH, "(//div[@class='filter-options-title' and @tabindex='0'])[12]")
price_option_loc = (By.CSS_SELECTOR, "a[href*='eco-friendly.html?price=10-20']")
products_prices_loc = (By.XPATH, "//li[@class='item product product-item']//span[@class='price']")
