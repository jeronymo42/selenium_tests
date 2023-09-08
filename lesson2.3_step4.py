from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .calc_func import calc

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который нажимает на кнопку
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    
    # Код, который обрабатывает alert
    browser.switch_to.alert.accept()

    # Получаем значение и рассчитываем ответ
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    # Отправляем форму с результатом
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
