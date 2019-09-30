import unittest
from dogFinderUITests import DogFinderUITestCases

test_map_element = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_dogs_toggle_button = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_parks_toggle_button = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)
test_parks_and_dogs_icons_counts = unittest.TestLoader().loadTestsFromTestCase(DogFinderUITestCases)

test_suite = unittest.TestSuite\
    ([test_map_element, test_dogs_toggle_button, test_parks_toggle_button, test_parks_and_dogs_icons_counts])

unittest.TextTestRunner(verbosity=2).run(test_suite)