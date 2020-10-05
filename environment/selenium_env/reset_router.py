from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = "http://admin:admin@192.168.1.3"

value1 = 'select[id=funcs]'
value2 = 'select[id=schools]'
value3 = '[name="UN"]'
value4 = '[name="PW"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    browser.get('/userRpm/SysRebootRpm.htm')
    button = browser.find_element_by_css_selector('[id="a55"]')
    button.click()

    try:
        xpath = 'button[title="Продолжить"]'
        button = browser.find_element_by_css_selector(xpath)
        button.click()
    except: pass

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()