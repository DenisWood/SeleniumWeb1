import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    selector = 'label [class="nowrap"]:nth-child(2)'
    x_element = browser.find_element_by_css_selector(selector)
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_tag_name('input[id="answer"]')
    input.send_keys(y)

    sel_check = 'input[id="robotCheckbox"]'
    option1 = browser.find_element_by_css_selector(sel_check)
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);") #скролим страницу


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