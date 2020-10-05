#заполняем длинную форму
from selenium import webdriver
import time

link_l = "http://suninjuly.github.io/huge_form.html"


try:
    browser = webdriver.Chrome()
    browser.get(link_l)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # вывод ответа в консоль
    alert = browser.switch_to.alert
    alert_text = alert.text
    # validate the alert text
    alert.accept()

    print(alert_text.split()[-1])
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



