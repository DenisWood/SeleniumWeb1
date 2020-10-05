# поиск ссылок по тексту или по подстроке

from selenium import webdriver
import math
import time

link_find = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_find)
link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    #поиск ссылки по тексту link_find
    link = browser.find_element_by_link_text(link_find)

    # поиск ссылки по подстроке link_find
    #link = browser.find_element_by_partial_link_text("examples")

    link.click()

    input1 = browser.find_element_by_tag_name('input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
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



