import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_laptop(browser):
    browser.get("https://www.ebay.com/")

    search_box = browser.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
    search_box.send_keys("Laptop")
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='srp-controls__count-heading']")))

    assert browser.find_element(By.XPATH, "//a[text()='Laptops & Netbooks']")

def test_check_product_availability(browser):
    browser.get("https://www.ebay.com/")

    search_box = browser.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
    search_box.send_keys("Dell XPS 13")
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='srp-controls__count-heading']")))

    first_result = browser.find_element(By.XPATH, "//li[contains(@class, 's-item')]//a")
    first_result.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@id='itemTitle']")))

    availability_text = browser.find_element(By.XPATH, "//span[contains(text(), 'More than 10 available')]").text
    assert "More than 10 available" in availability_text
