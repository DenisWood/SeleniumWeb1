# Заполнение формы на странице

from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

value1 = 'input[name="first_name"]'
value2 = 'input[name="last_name"]'
value3 = 'input[name="firstname"]'
value4 = 'input[name="firstname"][id="country"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_tag_name(value2)
    #input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_tag_name(value3)
    #input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element_by_tag_name(value4)
    #browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#find_elements_by_css_selector;
#find_elements_by_xpath;
#find_elements_by_name;
#find_elements_by_tag_name;
#find_elements_by_class_name;
#find_elements_by_link_text;
#find_elements_by_partial_link_text.