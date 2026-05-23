from playwright.sync_api import expect
from config import config


class LoginPage:

    def __init__(self, page):

        self.page = page

        self.email_input = page.get_by_placeholder(
            "Enter your mail"
        )

        self.password_input = page.get_by_placeholder(
            "Enter your password "
        )

        self.login_button = page.get_by_role(
            "button",
            name="Sign in"
        )

    def load(self):

        self.page.goto(config.BASE_URL)

    def login(self, email, password):

        expect(self.email_input).to_be_visible()

        self.email_input.fill(email)

        expect(self.password_input).to_be_visible()

        self.password_input.fill(password)

        expect(self.login_button).to_be_enabled()

        self.login_button.click()