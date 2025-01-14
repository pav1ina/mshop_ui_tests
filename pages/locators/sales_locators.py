from selenium.webdriver.common.by import By

hoodies_link_loc = (By.LINK_TEXT, 'Hoodies and Sweatshirts')
hoodies_title_loc = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
hoodies_breadcrumbs_loc = (By.CSS_SELECTOR, "div.breadcrumbs ul.items")
search_field_loc = (By.ID, 'search')
page_title_after_search_loc = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
error_loc = (By.XPATH, "//div[@class='message notice']/child::div")
