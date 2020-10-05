# Заполнение формы на странице XPath

from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

value1 = 'input[name="first_name"]'
value2 = 'input[name="last_name"]'
value3 = 'input[name="firstname"]'
value4 = 'input[name="firstname"][id="country"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    #button = browser.find_element_by_css_selector("button.btn")
    xpath = "button[type='submit']"
    button = browser.find_element_by_css_selector(xpath)

    xpath = "//button[text()='Submit']"
    xpath = '//button[@type="submit"]'
    xpath = "//button[contains(text(), 'Отправить')]"
    xpath = '//button[text()="Отправить"]'
    button = browser.find_element_by_xpath(xpath)
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