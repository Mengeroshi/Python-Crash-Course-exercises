import unittest
from city_function import city_country

class City_test(unittest.TestCase):
    """ dude"""
    def test_city_country(self):
        testing_cities = city_country("berlin", "alemania")
        self.assertEqual(testing_cities, "Berlin, Alemania")

    if __name__ == "__main__":
        unittest.main()