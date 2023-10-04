from secrets import LOGIN, PASSWORD
from selenium.webdriver.common.by import By
import pytest
import time
import math

link_list = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('link', link_list)
def test_step(browser, link):
    browser.get(link)
    time.sleep(5)
    enter_button = browser.find_element(By.ID, "ember33")
    enter_button.click()
    time.sleep(3)
    login_field = browser.find_element(By.ID, "id_login_email")
    login_field.send_keys(LOGIN)
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys(PASSWORD)
    login_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    login_button.click()
    time.sleep(5)
    answer_area = browser.find_element(By.CLASS_NAME, "textarea")
    answer = math.log(int(time.time()))
    answer_area.send_keys(answer)
    answer_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    answer_button.click()
    time.sleep(8)