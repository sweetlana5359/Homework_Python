from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, 'button')
    start_button.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'finish'), "Hello World!")
    )
    driver.save_screenshot('full_screen.png')
    hello_element = driver.find_element(By.CSS_SELECTOR, '#finish')
    assert hello_element.text == 'Hello World!'
    driver.quit()
