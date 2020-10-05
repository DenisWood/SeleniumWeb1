#Работа с окнами https://learn.javascript.ru/alert-prompt-confirm
import time
from selenium import webdriver
import math
# вызов окна с помощью JS:
#alert('Hello!');

# переключаемся на окно, нажимаем кнопку OK:
#alert = browser.switch_to.alert

# получаем текст из окна:
#alert = browser.switch_to.alert
#alert_text = alert.text

# нажатие кнопки от ОK:
#alert.accept()

# нажатие кнопки от Отмена:
# confirm.dismiss()

#Чтобы ввести текст, используйте метод send_keys():
#prompt.send_keys("My answer")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
    time.sleep(3)

    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(3)

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
