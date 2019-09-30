import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import requests
import jsonpath


class DogFinderUITestCases(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create new chrome instance
        inst.driver = webdriver.Chrome('chromedriver')
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to application
        inst.driver.get("http://sudden-cakes.surge.sh/")

    def test_map_element(self):
        # Ensure the map element renders on the application's web page
        self.assertTrue(self.is_element_present(By.XPATH, "//*[@id='map-container']/div[2]/canvas"))

    def test_dogs_toggle_button(self):
        # Test the toggle functionality and make sure only dogs and/or parks are being rendered when appropriate
        dogs_button = self.driver.find_element_by_xpath("//div[text()='Dogs']")
        dogs_button.click()
        dog_icons = self.driver.find_elements_by_xpath("//div[starts-with(@class,'dog-marker')]")

        for icon in dog_icons:

            self.assertFalse(icon.is_displayed())

    def test_parks_toggle_button(self):
        # Test the toggle functionality and make sure only dogs and/or parks are being rendered when appropriate
        parks_button = self.driver.find_element_by_xpath("//div[text()='Parks']")
        parks_button.click()
        park_icons = self.driver.find_elements_by_xpath("//div[starts-with(@class,'park-marker')]")

        for icon in park_icons:
            self.assertFalse(icon.is_displayed())

    def test_parks_and_dogs_icons_counts(self):
        dogs = "http://dogfinder.emboldhealth.com/dogs?limit=100"
        parks = "http://dogfinder.emboldhealth.com/parks?limit=20"

        response_dogs = jsonpath.jsonpath(requests.get(url=dogs).json(), 'results')
        response_parks = jsonpath.jsonpath(requests.get(url=parks).json(), 'results')

        dogs_count = response_dogs[0].__len__()
        parks_count = response_parks[0].__len__()

        parks_button = self.driver.find_element_by_xpath("//div[text()='Parks']")
        parks_button.click()
        dog_icons = self.driver.find_elements_by_xpath("//div[starts-with(@class,'dog-marker')]")

        self.assertTrue(dog_icons.__len__() == dogs_count)

        parks_button.click()
        dogs_button = self.driver.find_element_by_xpath("//div[text()='Dogs']")
        dogs_button.click()

        park_icons = self.driver.find_elements_by_xpath("//div[starts-with(@class,'park-marker')]")

        self.assertTrue(park_icons.__len__() == parks_count)

    @classmethod
    def tearDown(inst):
        # close browser
        inst.driver.quit()

    def is_element_present(self, how, what):
        """
        Helper method to confirm presence of element on screen
        :param how: by locator type
        :param what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def element_does_not_exist(self):
        with self.assertRaises(NoSuchElementException):
            self.driver.find_elements_by_xpath("locator")

if __name__ == '__main__':
    unittest.main(verbosity=2)
