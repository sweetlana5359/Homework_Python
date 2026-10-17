from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get('https://httpbin.qa-territory.online/forms/post')
    sleep(2)
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Анна")
    click_button = driver.find_element(By.CSS_SELECTOR, 'button')
    click_button.click()
    sleep(2)
    assert (
        driver.current_url == 'https://httpbin.qa-territory.online/post'
        )
    driver.quit()
