from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from calc_func import calc

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(num)
    field = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
