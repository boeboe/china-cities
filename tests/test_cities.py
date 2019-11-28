"""Package to test Cities """
import unittest
import china_cities

class CitiesTest(unittest.TestCase):
    """Class to test Cities """

    def test_constructor(self):
        '''Test function '''
        city = china_cities.City(name_en="NAME_EN", name_cn="NAME_CN", province="PROVINCE")
        self.assertEqual(city.name_en, "NAME_EN")
        self.assertEqual(city.name_cn, "NAME_CN")
        self.assertEqual(city.province, "PROVINCE")

    def test_get_cities(self):
        '''Test function '''
        cities = china_cities.get_cities()
        self.assertEqual(len(cities), 674)
        for city in cities:
            self.assertIsNotNone(city)
            self.assertTrue(city)
            self.assertTrue(isinstance(city, china_cities.City))
            self.assertTrue(city.name_en)
            self.assertTrue(city.name_cn)
            self.assertTrue(city.province)

    def test_get_cities_en(self):
        '''Test function '''
        cities_en = china_cities.get_cities_en()
        self.assertEqual(len(cities_en), 674)
        for city_en in cities_en:
            self.assertIsNotNone(city_en)
            self.assertTrue(city_en)
            self.assertTrue(isinstance(city_en, str))

    def test_get_cities_cn(self):
        '''Test function '''
        cities_cn = china_cities.get_cities_cn()
        self.assertEqual(len(cities_cn), 674)
        for city_cn in cities_cn:
            self.assertIsNotNone(city_cn)
            self.assertTrue(city_cn)
            self.assertTrue(isinstance(city_cn, str))

    def test_get_cities_by_province(self):
        '''Test function '''
        cities = china_cities.get_cities_by_province("Anhui")
        self.assertTrue(len(cities) > 0)
        self.assertEqual(len(cities), 23)

    def test_get_provinces(self):
        '''Test function '''
        provinces = china_cities.get_provinces()
        self.assertTrue(len(provinces) > 0)
        self.assertEqual(len(provinces), 34)
