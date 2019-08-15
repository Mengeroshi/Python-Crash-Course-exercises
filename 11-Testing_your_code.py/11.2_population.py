import unittest
from city_function_pop import city_country_d

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        mono = city_country_d("berlin", "alemania", 82_000_000)
        self.assertEqual(mono, "Berlin, Alemania. -Population: 82000000")

if __name__ == "__main__":
    unittest.main()