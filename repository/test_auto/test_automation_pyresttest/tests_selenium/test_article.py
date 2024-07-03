import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_create_article(driver):
    driver.get("http://localhost:8080/articles/new")
    driver.find_element(By.NAME, "title").send_keys("New Article")
    driver.find_element(By.NAME, "content").send_keys("Article content")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    assert "New Article" in driver.page_source

def test_edit_article(driver):
    driver.get("http://localhost:8080/articles/1/edit")
    driver.find_element(By.NAME, "title").clear()
    driver.find_element(By.NAME, "title").send_keys("Updated Title")
    driver.find_element(By.NAME, "content").clear()
    driver.find_element(By.NAME, "content").send_keys("Updated content")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    assert "Updated Title" in driver.page_source

def test_delete_article(driver):
    driver.get("http://localhost:8080/articles/1")
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    driver.switch_to.alert.accept()
    assert "Article not found" in driver.page_source
