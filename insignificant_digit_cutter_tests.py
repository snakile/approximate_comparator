import unittest
from insignificant_digit_cutter import *


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_cut_insignificant_digits_integer(self):
        self.assertEqual(7, cut_insignificant_digits(7, places=3))
    
    def test_cut_insignificant_digits_cut_nothing(self):
        self.assertEqual(12.3334, cut_insignificant_digits(12.3334, places=4))
        self.assertEqual(12.3334, cut_insignificant_digits(12.3334, places=6))
    
    def test_cut_insignificant_digits_cut_one(self):
        self.assertEqual(12.333, cut_insignificant_digits(12.3334, places=3))
    
    def test_cut_insignificant_digits_leave_one(self):
        self.assertEqual(12.3, cut_insignificant_digits(12.3334, places=1))
    
    def test_cut_insignificant_digits_cut_all(self):
        self.assertEqual(12.0, cut_insignificant_digits(12.3334, places=0))
    
    def test_cut_insignificant_digits_recursively_integer(self):
        self.assertEqual(7, cut_insignificant_digits_recursively(7, places=3))
        
    def test_cut_insignificant_digits_recursively_float(self):
        self.assertEqual(12.3, cut_insignificant_digits_recursively(12.3334, places=1))
    
    def test_cut_insignificant_digits_recursively_flat_list(self):
        self.assertEqual([12.1, 12.2, 12.3],
                         cut_insignificant_digits_recursively([12.1, 12.21, 12.321], places=1))
    
    def test_cut_insignificant_digits_recursively_flat_tuple(self):
        self.assertEqual((12.1, 12.2, 12.3),
                         cut_insignificant_digits_recursively((12.1, 12.21, 12.321), places=1))
    
    def test_cut_insignificant_digits_recursively_flat_set(self):
        self.assertEqual({12.1, 12.2, 12.3},
                         cut_insignificant_digits_recursively({12.1, 12.21, 12.321}, places=1))
    
    def test_cut_insignificant_digits_recursively_flat_dict(self):
        flat_dict = {12.123: 13.231, 7: 8.5, 0.1234: 0.123}
        flat_dict_cut_expected = {12.12: 13.23, 7: 8.5, 0.12: 0.12}
        flat_dict_cut_actual = cut_insignificant_digits_recursively(flat_dict, places=2)
        self.assertEqual(flat_dict_cut_expected, flat_dict_cut_actual)
    
    def test_cut_insignificant_digits_recursively_list_of_tuples(self):
        list_of_tuples = [(12.123, 13.231, 14.321), (7, 8.5), (0.1234, 0.123, 100.100)]
        list_of_tuples_cut_expected = [(12.12, 13.23, 14.32), (7, 8.5), (0.12, 0.12, 100.10)]
        list_of_tuples_cut_actual = cut_insignificant_digits_recursively(list_of_tuples, places=2)
        self.assertEqual(list_of_tuples_cut_expected, list_of_tuples_cut_actual)
    
    def test_cut_insignificant_digits_recursively_tuple_of_tuples(self):
        tuple_of_tuples = ((12.123, 13.231, 14.321), (7, 8.5), (0.1234, 0.123, 100.100))
        tuple_of_tuples_cut_expected = ((12.12, 13.23, 14.32), (7, 8.5), (0.12, 0.12, 100.10))
        tuple_of_tuples_cut_actual = cut_insignificant_digits_recursively(tuple_of_tuples, places=2)
        self.assertEqual(tuple_of_tuples_cut_expected, tuple_of_tuples_cut_actual)
        
    def test_cut_insignificant_digits_recursively_tuple_of_sets(self):
        tuple_of_sets = ({12.123, 13.231, 14.321}, {7, 8.5}, {0.1234, 0.123, 100.100})
        tuple_of_sets_cut_expected = ({12.12, 13.23, 14.32}, {7, 8.5}, {0.12, 0.12, 100.10})
        tuple_of_sets_cut_actual = cut_insignificant_digits_recursively(tuple_of_sets, places=2)
        self.assertEqual(tuple_of_sets_cut_expected, tuple_of_sets_cut_actual)
    
    def test_cut_insignificant_digits_recursively_list_of_tuples_of_sets(self):
        tuple_of_sets1 = ({12.123, 13.231, 14.321}, {7, 8.5}, {0.1234, 0.123, 100.100})
        tuple_of_sets2 = ({7.123, 1.231, 4.321}, {7.8888, 8.5}, {0.1234})
        tuple_of_sets3 = ({0, 1.231, 4}, {7.8788, 8.5})
        list_of_tuples_of_sets = [tuple_of_sets1, tuple_of_sets2, tuple_of_sets3]
        tuple_of_sets1_cut_expected = ({12.12, 13.23, 14.32}, {7, 8.5}, {0.12, 0.12, 100.10})
        tuple_of_sets2_cut_expected = ({7.12, 1.23, 4.32}, {7.88, 8.5}, {0.12})
        tuple_of_sets3_cut_expected = ({0, 1.23, 4}, {7.87, 8.5})
        list_of_tuples_of_sets_cut_expected = [tuple_of_sets1_cut_expected, tuple_of_sets2_cut_expected, tuple_of_sets3_cut_expected]
        list_of_tuples_of_sets_cut_actual = cut_insignificant_digits_recursively(list_of_tuples_of_sets, places=2)
        self.assertEqual(list_of_tuples_of_sets_cut_expected, list_of_tuples_of_sets_cut_actual)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
