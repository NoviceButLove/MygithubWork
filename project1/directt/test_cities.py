from Testfunction_pratise import bing
import unittest

class CountryTestCase(unittest.TestCase):
    '''测试函数练习'''
    def test_city_country_test(self):
        formatted = bing('beijing','china')
        self.assertEqual(formatted,'Beijing,China')

    def test_city_country_population(self):
        formatted1 = bing('beijing','china',population=14)
        self.assertEqual(formatted1,'Beijing,China - Population = 14')
if __name__ == "__main__":
    unittest.main()