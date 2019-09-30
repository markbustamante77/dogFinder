import unittest
import requests
import jsonpath


class DogFinderAPITestCases(unittest.TestCase):

    def test_get_dogs_response(self):
        dogs = "http://dogfinder.emboldhealth.com/dogs"
        response_dogs = jsonpath.jsonpath(requests.get(url=dogs).json(), 'results')
        default_list_count = response_dogs[0].__len__()
        count = jsonpath.jsonpath(requests.get(url=dogs).json(), 'count')

        self.assertTrue(count[0] == 100)
        self.assertTrue(default_list_count == 10)

    def test_get_limit_dogs_response(self):
        dogs_limit = "http://dogfinder.emboldhealth.com/dogs?limit=100"
        response_dogs_limit = jsonpath.jsonpath(requests.get(url=dogs_limit).json(), 'results')
        limit_list_count = response_dogs_limit[0].__len__()
        count = jsonpath.jsonpath(requests.get(url=dogs_limit).json(), 'count')

        self.assertTrue(limit_list_count == count[0])

    def test_offset_dogs_response(self):
        dogs_limit_4_offset_0 = "http://dogfinder.emboldhealth.com/dogs?limit=4"
        dogs_limit_3_offset_1 = "http://dogfinder.emboldhealth.com/dogs?limit=3&offset=1"

        resp_dogs_limit_4_offset_0 = jsonpath.jsonpath(requests.get(url=dogs_limit_4_offset_0).json(), 'results')

        remove_list_0 = resp_dogs_limit_4_offset_0.pop(0)
        remove_dog_0 = remove_list_0.pop(0)

        resp_dogs_limit_3_offset_1 = jsonpath.jsonpath(requests.get(url=dogs_limit_3_offset_1).json(), 'results')
        remove_class_list = resp_dogs_limit_3_offset_1.pop(0)

        self.assertTrue(remove_list_0 == remove_class_list)

    def test_get_parks_response(self):
        parks = "http://dogfinder.emboldhealth.com/parks"
        response_parks = jsonpath.jsonpath(requests.get(url=parks).json(), 'results')
        default_list_count = response_parks[0].__len__()
        count = jsonpath.jsonpath(requests.get(url=parks).json(), 'count')

        self.assertTrue(count[0] == 20)
        self.assertTrue(default_list_count == 10)

    def test_get_limit_parks_response(self):
        parks_limit = "http://dogfinder.emboldhealth.com/parks?limit=20"
        response_parks_limit = jsonpath.jsonpath(requests.get(url=parks_limit).json(), 'results')
        limit_list_count = response_parks_limit[0].__len__()
        count = jsonpath.jsonpath(requests.get(url=parks_limit).json(), 'count')

        self.assertTrue(limit_list_count == count[0])

    def test_offset_parks_response(self):
        parks_limit_4_offset_0 = "http://dogfinder.emboldhealth.com/parks?limit=4"
        parks_limit_3_offset_1 = "http://dogfinder.emboldhealth.com/parks?limit=3&offset=1"

        resp_parks_limit_4_offset_0 = jsonpath.jsonpath(requests.get(url=parks_limit_4_offset_0).json(), 'results')

        remove_list_0 = resp_parks_limit_4_offset_0.pop(0)
        remove_park_0 = remove_list_0.pop(0)

        resp_parks_limit_3_offset_1 = jsonpath.jsonpath(requests.get(url=parks_limit_3_offset_1).json(), 'results')
        remove_class_list = resp_parks_limit_3_offset_1.pop(0)

        self.assertTrue(remove_list_0 == remove_class_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)