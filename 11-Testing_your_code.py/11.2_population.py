import unittest
from city_function_pop import city_country_d

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        mono = city_country_d("berlin", "alemania")
        self.assertEqual(mono, "Berlin, Alemania")

    if __name__ == "__main__":
        unittest.main()