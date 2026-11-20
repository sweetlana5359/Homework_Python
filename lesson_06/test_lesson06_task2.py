from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get('https://gitflic.ru/')
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'ODcyMjAyYjgtNzJmYS00OTZiLWEwYjItOWIxNzA4MWJhNjQ2',
        'domain': 'gitflic.ru'
    })
    driver.refresh()
    driver.get('https://gitflic.ru/user/fob_11_2014')
    url_user_1 = driver.current_url
    driver.delete_all_cookies()
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'ZDYzM2EwNGMtMzczOC00OWZmLWJjZTAtOGY1OTRlNzQ3MjQ4',
        'domain': 'gitflic.ru'
        })
    driver.refresh()
    driver.get('https://gitflic.ru/user/mj_chicago_26')
    url_user_2 = driver.current_url
    assert url_user_1 != url_user_2
    driver.quit()
