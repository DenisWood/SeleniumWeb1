import os
import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    selector = 'input[name="firstname"]'
    input = browser.find_element_by_tag_name(selector)
    input.send_keys('Вася')

    selector = 'input[name="lastname"]'
    input = browser.find_element_by_tag_name(selector)
    input.send_keys('Иванов')

    selector = 'input[name="email"]'
    input = browser.find_element_by_tag_name(selector)
    input.send_keys('kjhfkjhfk@mail.com')

    selector = 'input[id="file"]'
    element = browser.find_element_by_tag_name(selector)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

finally:
    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()
    print(alert_text.split()[-1])

    time.sleep(10)
    browser.quit()

# Проходит по всем селекторам import и заполняет поля
#for inp in browser.find_elements_by_css_selector(".form-group input"):
#    inp.send_keys("data")

# или так:
#inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]
#for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
#    element.send_keys(value)