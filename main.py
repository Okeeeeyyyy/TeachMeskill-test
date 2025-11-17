import pytest
from selenium.webdriver.common.by import By

# url = "https://letcode.in/test"
url = "https://www.wildberries.by/"


@pytest.mark.smoke
def test_locators(driver):
    driver.get(url)
    # el = driver.find_elements(By.ID, "account-register")
    el = driver.find_elements(By.NAME, "search")[-1]
    el.send_keys("hello")

    el = driver.find_element(By.PARTIAL_LINK_TEXT, "login")
    el = driver.find_element(By.LINK_TEXT, "login")
    el.click()

    el = driver.find_element(By.TAG_NAME, "header")
    el.click()

    el = driver.find_elements(By.CLASS_NAME, "entry-section container")
    el.click()
