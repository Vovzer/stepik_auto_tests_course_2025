from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Открываем страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

try:
    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("John")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("johndoe@example.com")

    # Создаем временный файл .txt
    with open("test_file.txt", "w") as file:
        file.write("Hello, world!")

    # Получаем путь к файлу
    file_path = os.path.abspath("test_file.txt")

    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждем, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()

    # Удаляем временный файл
    os.remove("test_file.txt")
