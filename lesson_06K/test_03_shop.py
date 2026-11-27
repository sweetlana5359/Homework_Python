from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox()
    driver.get('https://www.saucedemo.com/')
    input_user_name = driver.find_element(By.ID, 'user-name')
    input_user_name.send_keys('standard_user')
    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys('secret_sauce')
    submit_button = driver.find_element(By.CLASS_NAME, 'submit-button')
    submit_button.click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    driver.find_element(By.ID, 'checkout').click()
    input_first_name = driver.find_element(By.ID, 'first-name')
    input_first_name.send_keys('Anna')
    input_last_name = driver.find_element(By.ID, 'last-name')
    input_last_name.send_keys('Black')
    input_postal_code = driver.find_element(By.ID, 'postal-code')
    input_postal_code.send_keys('11223344')
    submit_button = driver.find_element(By.CLASS_NAME, 'submit-button')
    submit_button.click()
    total_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    driver.quit()
    assert '$58.29' in total_text
