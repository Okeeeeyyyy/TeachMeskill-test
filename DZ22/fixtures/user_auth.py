import pytest

from DZ22.pages.main_page import Main


@pytest.fixture(scope="class")
def user_login(browser):
    m = Main(browser)
    m.user_login()
