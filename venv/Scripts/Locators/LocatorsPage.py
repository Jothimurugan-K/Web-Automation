import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class InputFormsPage(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.input_forms_by_link_text = "Input Forms"
        self.simple_form_demo_by_link_text = "Simple Form Demo"
        self.single_input_field_by_id = "user-message"
        self.show_message_button_by_xpath = '//*[@id="get-input"]/button'
        self.display_check = "display"
        self.displayvalue_check = "displayvalue"
        self.enter_a_by_id = "sum1"
        self.enter_b_by_id = "sum2"
        self.get_total_by_xpath = '//*[@id="gettotal"]/button'

    def click_input_forms_link(self):
        self.driver.find_element_by_link_text(self.input_forms_by_link_text).click()
        time.sleep(5)

    def click_simple_form_demo(self):
        self.driver.find_element_by_link_text(self.simple_form_demo_by_link_text).click()
        time.sleep(5)

    def single_input_field(self, single_input_message):
        self.driver.find_element_by_id(self.single_input_field_by_id).send_keys(single_input_message)
        self.driver.find_element_by_xpath(self.show_message_button_by_xpath).click()
        self.single_input_field_result = self.driver.find_element_by_id(self.display_check).text
        self.assertEqual(self.single_input_field_result, single_input_message, "Single input field not matching...")

    def two_input_fields(self, enter_a, enter_b):
        self.driver.find_element_by_id(self.enter_a_by_id).send_keys(enter_a)
        self.driver.find_element_by_id(self.enter_b_by_id).send_keys(enter_b)
        self.actual_two_input_fields_result = enter_a + enter_b
        self.driver.find_element_by_xpath(self.get_total_by_xpath).click()
        self.two_input_field_result = self.driver.find_element_by_id(self.displayvalue_check).text
        self.assertEqual(self.two_input_field_result,str( self.actual_two_input_fields_result), "Two input field not matching...")


class CheckboxDemoPage(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.input_forms_by_link_text = "Input Forms"
        self.check_box_demo_by_link_text = "Checkbox Demo"
        self.single_check_box_by_id = 'isAgeSelected'
        self.multiple_check_box_by_xpath = "//*[@class='cb1-element']"

    def click_input_forms_link(self):
        self.driver.find_element_by_link_text(self.input_forms_by_link_text).click()
        time.sleep(2)

    def click_check_box_demo(self):
        self.driver.find_element_by_link_text(self.check_box_demo_by_link_text).click()
        time.sleep(2)

    def click_single_check_box(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.single_check_box_by_id).click()

    def click_multiple_check_box(self):
        for elem in self.driver.find_elements_by_xpath(self.multiple_check_box_by_xpath):
            elem.click()
#             time.sleep(1)

class RadioButtonPage(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.input_forms_by_link_text = "Input Forms"
        self.radio_button_demo_by_link_text = "Radio Buttons Demo"
        self.click_radio_button = "//input[contains(@value,'Male')]"
        self.click_button_check = "buttoncheck"
        self.result_xpath = "//*[@class='radiobutton']"

    def click_input_forms_link(self):
        self.driver.find_element_by_link_text(self.input_forms_by_link_text).click()
        time.sleep(2)

    def click_radio_box_demo(self):
        self.driver.find_element_by_link_text(self.radio_button_demo_by_link_text).click()
        time.sleep(2)

    def radio_button_click(self):
        self.radio_clicked = self.driver.find_element_by_xpath(self.click_radio_button).click()
        time.sleep(2)

    def verify_change_radio_button(self):
        self.driver.find_element_by_id(self.click_button_check).click()
        self.actual_result = self.driver.find_element_by_xpath(self.result_xpath).text
        self.assertEqual(self.actual_result, "Radio button 'Female' is checked", "Failed...")

class DropDownPage(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.input_forms_by_link_text = "Input Forms"
        self.drop_down_by_link_text = "Select Dropdown List"
        self.drop_down_click = "select-demo"
        self.select_some_day = "Wednesday"

    def click_input_forms_link(self):
        self.driver.find_element_by_link_text(self.input_forms_by_link_text).click()
        time.sleep(2)

    def click_drop_down_box_demo(self):
        self.driver.find_element_by_link_text(self.drop_down_by_link_text).click()
        time.sleep(2)

    def select_drop_down(self):
        self.driver.find_element_by_id(self.drop_down_click).click()
        select = Select(self.driver.find_element_by_id(self.drop_down_click).click())
        select.select_by_value(self.select_some_day)

class DragandDrop(unittest.TestCase):
    pass

class ProgressBar(unittest.TestCase):
    pass

class Alert(unittest.TestCase):
    pass

class BrowserNavigation(unittest.TestCase):
    pass

class Screenshot(unittest.TestCase):
    pass

















