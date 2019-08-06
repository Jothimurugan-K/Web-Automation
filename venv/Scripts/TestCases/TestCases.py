import unittest
import time
from selenium import webdriver
from Scripts.Locators.LocatorsPage import DropDownPage


class AllTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.seleniumeasy.com/test")
        self.driver.maximize_window()

    def test_single_input_form(self):
        driver = self.driver
        single_input_message = "sample message"
        enter_a = 10
        enter_b = 20
        InputFormObj = InputFormsPage(driver)
        InputFormObj.click_input_forms_link()
        InputFormObj.click_simple_form_demo()
        InputFormObj.single_input_field(single_input_message)
        InputFormObj.two_input_fields(enter_a, enter_b)

    def test_check_box_demo(self):
        driver = self.driver
        CheckBoxObj = CheckboxDemoPage(driver)
        CheckBoxObj.click_input_forms_link()
        CheckBoxObj.click_check_box_demo()
        CheckBoxObj.click_single_check_box()
        CheckBoxObj.click_multiple_check_box()

    def test_radio_button_demo(self):
        driver = self.driver
        RadioButtonObj = RadioButtonPage(driver)
        RadioButtonObj.click_input_forms_link()
        RadioButtonObj.click_radio_box_demo()
        RadioButtonObj.radio_button_click()
        RadioButtonObj.verify_change_radio_button()

    def test_drop_down_demo(self):
        driver = self.driver
        DropDownObj = DropDownPage(driver)
        DropDownObj.click_input_forms_link()
        DropDownObj.click_drop_down_box_demo()
        DropDownObj.select_drop_down()

    def test_radio_button_demo(self):
        pass

    def test_drop_down_demo(self):
        pass

    def test_progress_bar_demo(self):
        pass

    def test_alert_demo(self):
        pass

    def test_browser_navigation_demo(self):
        pass

    @classmethod
    def tearDownClass(self):
        time.sleep(4)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
