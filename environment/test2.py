from selenium import webdriver
import time

link = "https://sgo.rso23.ru/?AL=Y"

value1 = 'select[id=funcs]'
value2 = 'select[id=schools]'
value3 = '[name="UN"]'
value4 = '[name="PW"]'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    browser.find_element_by_tag_name(value1).click()
    time.sleep(1)
    browser.find_element_by_tag_name("[id='funcs'] [value='2']").click()
    #browser.find_element_by_css_selector("option:nth-child(2)").click()
    time.sleep(1)
    browser.find_element_by_tag_name(value2).click()
    time.sleep(1)
    browser.find_element_by_tag_name("[value='4972']").click()
    time.sleep(1)
    input3 = browser.find_element_by_tag_name(value3)
    input3.send_keys("оМалышевД1")
    input4 = browser.find_element_by_tag_name(value4)
    input4.send_keys("102938")
    xpath = "[class=button-login-title]"
    button = browser.find_element_by_css_selector(xpath)
    button.click()

    time.sleep(3)
    try:
        xpath = 'button[title="Продолжить"]'
        button = browser.find_element_by_css_selector(xpath)
        button.click()
    except: pass

    time.sleep(5)
    for i in range(2,7):
        pars_num = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]''' +f''':nth-child({i}) [class="num_subject ng-binding"]'''
        #pars_num = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]:nth-child({i}) [class="num_subject ng-binding"]'''
        str1 = browser.find_element_by_tag_name(pars_num).text

        pars_name = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]''' +f''':nth-child({i}) [class="subject ng-binding ng-scope"]'''
        #pars_name = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]:nth-child(2) [class="subject ng-binding ng-scope"]'''
        str2 = browser.find_element_by_tag_name(pars_name).text

        #pars_lesson = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]:nth-child(2) [class="hidden-mobile wrapper_three_dots"] [class="ng-binding ng-scope"]'''
        pars_lesson = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]''' +f''':nth-child({i}) [class="hidden-mobile wrapper_three_dots"]'''
        #pars_lesson = '''[ng-repeat="diaryDay in ctrl.data.diary.weekDays | limitTo: 3"]:nth-child(1) [ng-class="{'hidden-xs': !lesson.subjectName}"]:nth-child(2) [class="hidden-mobile wrapper_three_dots"]'''
        str3 = browser.find_element_by_tag_name(pars_lesson).text

        print(str1, str2, str3)


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()