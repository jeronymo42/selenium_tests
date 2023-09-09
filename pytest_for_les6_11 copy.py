from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def registration_test(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1_1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1_1.send_keys("Ivan")

    input1_2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input1_2.send_keys("Petrov")

    input1_3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input1_3.send_keys("I.Petrov@gmail.com")

    input2_3 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input2_3.send_keys("91111111")

    input2_4 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input2_4.send_keys("New York")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    return welcome_text_elt.text


def test_success():
    assert "Congratulations! You have successfully registered!" == registration_test(link1), 'Неуспешная регистрацию =('


def test_unsuccess():
    assert "Congratulations! You have successfully registered!" == registration_test(link2), 'Неуспешная регистрацию =('
