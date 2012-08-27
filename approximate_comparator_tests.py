import unittest
from approximate_comparator import *


class Test(unittest.TestCase):


    def test_integers_almost_equal(self):
        self.assertTrue(is_almost_equal(7, 7, places=3))
        self.assertFalse(is_almost_equal(6, 7, places=3))
    
    def test_strings_almost_equal(self):
        self.assertTrue(is_almost_equal('seven', 'seven', places=3))
        self.assertFalse(is_almost_equal('six', 'seven', places=3))
    
    def test_floats_almost_equal(self):
        self.assertTrue(is_almost_equal(7.1234, 7.12356, places=3))
        self.assertFalse(is_almost_equal(6.1234, 7.1334, places=3))
    
    def test_flat_lists_almost_equal(self):
        first = [12.1234, 21.00988, 7.4, 'hello', 42]
        second = [12.123456, 21.009, 7.40, 'hello', 42]
        self.assertTrue(is_almost_equal(first, second, places=3))
        self.assertTrue(is_almost_equal(first, second, places=2))
        self.assertTrue(is_almost_equal(first, second, places=1))
        self.assertFalse(is_almost_equal(first, second, places=4))
    
    def test_flat_tuples_almost_equal(self):
        first = (12.1234, 21.00988, 7.4, 'hello', 42)
        second = (12.123456, 21.009, 7.40, 'hello', 42)
        self.assertTrue(is_almost_equal(first, second, places=3))
        self.assertTrue(is_almost_equal(first, second, places=2))
        self.assertTrue(is_almost_equal(first, second, places=1))
        self.assertFalse(is_almost_equal(first, second, places=4))
    
    def test_flat_sets_almost_equal(self):
        first = {12.1234, 21.00988, 7.4, 'hello', 42}
        second = {12.123456, 21.009, 7.40, 'hello', 42}
        self.assertTrue(is_almost_equal(first, second, places=3))
        self.assertTrue(is_almost_equal(first, second, places=2))
        self.assertTrue(is_almost_equal(first, second, places=1))
        self.assertFalse(is_almost_equal(first, second, places=4))
    
    def test_flat_dicts_almost_equal(self):
        first = {'a': 12.1234, 777.7777: 21.00988, 123.0011: 7.4, 3: 'hello', 12.09876: 42}
        second = {'a': 12.12399, 777.7778: 21.009, 123.0012: 7.4, 3: 'hello', 12.09876: 42}
        self.assertTrue(is_almost_equal(first, second, places=3))
        self.assertTrue(is_almost_equal(first, second, places=2))
        self.assertTrue(is_almost_equal(first, second, places=1))
        self.assertFalse(is_almost_equal(first, second, places=4))
        
    def test_dic_mapping_tuples_to_lists_and_sets_almost_equal(self):
        tuple1_a = ('abc', 7.1234, 3.14)
        tuple1_b = ('abc', 7.123, 3.14)
        tuple2_a = (10, 7.0099)
        tuple2_b = (10, 7.009911)
        tuple3_a = (7.4321, 1.2)
        tuple3_b = (7.432, 1.2)
        value1_a = [0.5555, 'x', (7.123, 123.7)]
        value1_b = [0.5555, 'x', (7.12345, 123.7)]
        value2_a = [4.9999, 3.141, 3.14]
        value2_b = [4.999, 3.1413, 3.14]
        value3_a = {1.111, 2.222}
        value3_b = {1.111, 2.22222}
        
        dict_a = {tuple1_a: value1_a, tuple2_a: value2_a, tuple3_a: value3_a}
        dict_b = {tuple1_b: value1_b, tuple2_b: value2_b, tuple3_b: value3_b}
        
        self.assertTrue(is_almost_equal(dict_a, dict_b, places=3))
        self.assertTrue(is_almost_equal(dict_a, dict_b, places=2))
        self.assertTrue(is_almost_equal(dict_a, dict_b, places=1))
        self.assertFalse(is_almost_equal(dict_a, dict_b, places=4))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()