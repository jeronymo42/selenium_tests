from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from calc_func import calc

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#answer")
    checkbox.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    checkbox.click()

    checkbox = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    checkbox.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
