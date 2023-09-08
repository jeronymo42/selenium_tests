from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который нажимает на кнопку (откроется новое окно)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    
    # Переключаемся на новое окно
    browser.switch_to.window(browser.window_handles[1])

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
