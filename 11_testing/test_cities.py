import unittest
import city_functions

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        self.assertEquals(city_functions.city_format('santiago', 'chile'), 'Santiago, Chile')
    def test_city_country_population(self):
        self.assertEquals(city_functions.city_format('santiago', 'chile', '5000000'), 'Santiago, Chile - population 5000000')