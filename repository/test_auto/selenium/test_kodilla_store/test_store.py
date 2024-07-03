import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXPECTED_RESULTS = {
    "NoteBook": 2,
    "School": 1,
    "Brand": 1,
    "Business": 0,
    "Gaming": 1,
    "Powerful": 1
}

def search_and_get_result_count(driver, search_term):
    search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Szukaj...']")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section>article")))

    product_cards = driver.find_elements(By.CSS_SELECTOR, "section>article")
    return len(product_cards)

def test_store(browser):
    browser.get("https://kodilla.com/pl/test/store")

    for term, expected_count in EXPECTED_RESULTS.items():
        actual_count = search_and_get_result_count(browser, term)
        assert actual_count == expected_count, f"Expected {expected_count} results for '{term}', but found {actual_count}."

        term_lower = term.lower()
        actual_count_lower = search_and_get_result_count(browser, term_lower)
        assert actual_count_lower == expected_count, f"Expected {expected_count} results for '{term_lower}', but found {actual_count_lower}."

        term_upper = term.upper()
        actual_count_upper = search_and_get_result_count(browser, term_upper)
        assert actual_count_upper == expected_count, f"Expected {expected_count} results for '{term_upper}', but found {actual_count_upper}."
