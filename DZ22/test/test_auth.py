import pytest

from DZ22.pages.main_page import Main


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = Main(browser)
        m.user_login()
