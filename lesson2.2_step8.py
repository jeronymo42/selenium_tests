from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    input_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_name.send_keys("Ivan")
    input_lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_lastname.send_keys("Ivanov")
    input_email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_email.send_keys("ivan@gmail.com")

    input_file = browser.find_element(By.CSS_SELECTOR, "#file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input_file.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
