from selenium.webdriver.common.by import By


firstname_field_loc = (By.ID, 'firstname')
lastname_field_loc = (By.ID, 'lastname')
email_field_loc = (By.ID, 'email_address')
passw_field_loc = (By.ID, 'password')
repeat_passw_field_loc = (By.ID, 'password-confirmation')
create_button_loc = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
