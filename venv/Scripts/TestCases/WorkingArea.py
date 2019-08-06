import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
#
# driver.find_element_by_id("select-demo").click()
# Se
# Progress bar

# Drag and drop

# source = driver.find_element_by_xpath('//*[@id="todrag"]/span[1]')
# print(source.location)
# print(source.text)
# target = driver.find_element_by_xpath('//*[@id="mydropzone"]')
# print(target.location)
# actions = ActionChains(driver)
# actions.drag_and_drop_by_offset(source, 408-285, 453-472).perform()
# move = actions.drag_and_drop(source, target)
# # time.sleep(1)
# # move.perform()
# # print("pass")
# time.sleep(5)
#
# actions = ActionChains(driver)
#
# source = driver.find_element_by_xpath('//*[@id="slider1"]/div/input')
# print(source.location)
# actions.drag_and_drop_by_offset(source, 352+60, 379+60).perform()
# source.click()


# autoclose = driver.find_element_by_xpath("//*[@class='col-md-4' and @id='autoclosable-btn-success']")
# autoclose.click()
# time.sleep(5)
# alterwindow = driver.switch_to.alert
# alterwindow.accept()
# print("Alert accepted")


# try:
#     WebDriverWait(driver,5).until(EC.alert_is_present(),'Timed out waiting for alerts')
#     alterwindow = driver.switch_to.alert
#     alterwindow.accept()
#     print("Alert accepted")
# except TimeoutException:
#     print("no alerts")
# #print(alterwindow.text)
# #alterwindow.accept(

#
# ele = driver.find_element_by_css_selector('body')
# time.sleep(8)
# ele.send_keys(Keys.CONTROL+'all')
# ele.send_keys(Keys.CONTROL+'c')
# f = open("file.txt", "w")


driver.refresh()
time.sleep(5)
driver.find_element_by_link_text("Gmail").click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()


