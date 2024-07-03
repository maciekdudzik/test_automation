import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_amount(driver, search_term, expected_count):
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Szukaj...']")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='products row']")))

    results = driver.find_elements(By.XPATH, "//div[@class='products row']//div[@class='product']")
    actual_count = len(results)

    assert actual_count == int(expected_count), f"Expected {expected_count} results for '{search_term}', but found {actual_count}."

def test_store(browser):
    browser.get("https://kodilla.com/pl/test/store")

    assert_amount(browser, "Laptop", "3")
    assert_amount(browser, "NoteBook", "2")
    assert_amount(browser, "Gaming", "1")
    assert_amount(browser, "Course", "4")
    assert_amount(browser, "Programming", "5")
