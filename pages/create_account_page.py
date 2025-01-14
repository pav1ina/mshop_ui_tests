from selenium.webdriver.common.by import By
from pages.locators import create_account_locators as loc
from pages.base_page import BasePage


required_field_message_loc = (By.XPATH,
                              '//input[contains(@class, "required-entry")]/following-sibling::div[@class="mage-error"]')

existing_email_message_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

password_length_message_loc = (By.CSS_SELECTOR, 'div[id="password-error"]')


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def check_required_field_message(self, text):
        required_field_message = self.find(required_field_message_loc)
        assert required_field_message.text == text

    def check_existing_email_message(self, text):
        existing_email_message = self.find(existing_email_message_loc)
        print(existing_email_message.text)
        assert existing_email_message.text == text

    def check_password_length_validation_message(self, text):
        password_length_validation_message = self.find(password_length_message_loc)
        assert password_length_validation_message.text == text

    def fill_create_account_form(self, firstname, lastname, email, password, confirm_password):
        firstname_field = self.find(loc.firstname_field_loc)
        lastname_field = self.find(loc.lastname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.passw_field_loc)
        confirm_password_field = self.find(loc.repeat_passw_field_loc)
        create_account_button = self.find(loc.create_button_loc)
        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        create_account_button.click()
