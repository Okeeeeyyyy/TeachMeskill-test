from playwright.sync_api import Page

from DZ22.data.assertions import Assertions
from DZ22.data.constants import Constants
from DZ22.Locators.auth import Auth
from DZ22.pages.base import Base


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.input(Auth.USERNAME_INPUT, Constants.login)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)
        self.assertion.check_URL("inventory.html", "Wrong URL")
