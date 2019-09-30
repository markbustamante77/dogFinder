import unittest
from dogFinderUITests import DogFinderUITestCases
from dogFinderApiTests import DogFinderAPITestCases

test_map_element = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_dogs_toggle_button = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_parks_toggle_button = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_parks_and_dogs_icons_counts = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)

test_get_dogs_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)
test_get_limit_dogs_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)
test_offset_dogs_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)
test_get_parks_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)
test_get_limit_parks_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)
test_offset_parks_response = unittest.TestLoader().loadTestsFromTestCase(DogFinderAPITestCases)

test_suite = unittest.TestSuite([test_map_element, test_dogs_toggle_button, test_parks_toggle_button,
                                 test_parks_and_dogs_icons_counts, test_get_dogs_response, test_get_limit_dogs_response,
                                 test_offset_dogs_response, test_get_parks_response, test_get_limit_parks_response,
                                 test_offset_parks_response])

unittest.TextTestRunner(verbosity=2).run(test_suite)
