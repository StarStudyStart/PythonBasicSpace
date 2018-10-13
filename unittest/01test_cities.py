import unittest
from city_functions import city_country

class CityInfoTestCase(unittest.TestCase):
    '''测试city_country函数'''
    def test_city_country_info(self):
        '''能够正确的输出城市信息'''
        city_info = city_country('hefei','anhui','200w')
        self.assertEqual(city_info,'Hefei,Anhui - population 200w')
        
unittest.main()
