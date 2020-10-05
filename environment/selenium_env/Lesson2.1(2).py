import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    selector = 'img'
    #x_element = browser.find_element_by_css_selector(selector)
    x_element = browser.find_element_by_id("treasure")
    valuex = x_element.get_attribute("valuex")
    x = valuex
    y = calc(x)
    input = browser.find_element_by_tag_name('input[id="answer"]')
    input.send_keys(y)

    sel_check = 'input[id="robotCheckbox"]'
    option1 = browser.find_element_by_css_selector(sel_check)
    option1.click()

    sel_radio = 'input[id="robotsRule"]'
    option2 = browser.find_element_by_css_selector(sel_radio)
    option2.click()

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