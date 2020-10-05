#Работа с окнами https://learn.javascript.ru/alert-prompt-confirm
import time
from selenium import webdriver
import math
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти:
#browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок:
#new_window = browser.window_handles[1]
#first_window = browser.window_handles[0]

# Текущую вкладку можно узнать так::
#current_window = browser.current_window_handle

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    time.sleep(3)
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_tag_name('input[id="answer"]')
    input.send_keys(y)

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
