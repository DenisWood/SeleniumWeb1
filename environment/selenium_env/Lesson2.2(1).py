import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    selector = 'h2 [id="num1"]'
    num1 = browser.find_element_by_css_selector(selector).text
    selector = 'h2 [id="num2"]'
    num2 = browser.find_element_by_css_selector(selector).text
    print(num1, num2)
    sum = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_css_selector('select[id="dropdown"]'))
    select.select_by_value(sum)  # ищем элемент с текстом "Python"

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