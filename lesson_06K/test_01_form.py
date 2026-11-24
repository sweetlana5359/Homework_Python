from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    first_name = driver.find_element(By.NAME, 'first-name')
    first_name.send_keys('Иван')
    last_name = driver.find_element(By.NAME, 'last-name')
    last_name.send_keys('Петров')
    address = driver.find_element(By.NAME, 'address')
    address.send_keys('Ленина, 55-3')
    email = driver.find_element(By.NAME, 'e-mail')
    email.send_keys('test@skypro.com')
    phone_number = driver.find_element(By.NAME, 'phone')
    phone_number.send_keys('+7985899998787')
    city = driver.find_element(By.NAME, 'city')
    city.send_keys('Москва')
    country = driver.find_element(By.NAME, 'country')
    country.send_keys('Россия')
    job_position = driver.find_element(By.NAME, 'job-position')
    job_position.send_keys('QA')
    company = driver.find_element(By.NAME, 'company')
    company.send_keys('SkyPro')
    click_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    click_button.click()
    zip_code = driver.find_element(By.ID, 'zip-code')
    assert 'alert-danger' in zip_code.get_attribute('class')
    fieldes = ['first-name', 'last-name', 'address', 'e-mail',
               'phone', 'city', 'country', 'job-position', 'company']
    for field_id in fieldes:
        element = driver.find_element(By.ID, field_id)
        assert "alert-success" in element.get_attribute("class")
    driver.quit()
