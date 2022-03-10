import unittest

from datatransform.datatransform import *


class TestCase(unittest.TestCase):
    def setUp(self):
        self.setUpTestCases()


class TestDataTransform(TestCase):
    def setUpTestCases(self):
        self.df = pd.read_csv('inputs/bookings.csv')

    def test_calculate_age(self):
        self.assertEqual(calculate_age('2000-01-01'), 22)

    def test_exec_function(self):
        self.assertEqual(exec_function('birthdate_to_age', self.df, 'user_birthdate', 'foo'),
                         birthdate_to_age(self.df, 'user_birthdate', 'foo'))
        self.assertEqual(exec_function('hot_encoding', self.df, 'vehicle_category'),
                         hot_encoding(self.df, 'vehicle_category'))
        self.assertEqual(exec_function('fill_empty_values', self.df, 'km', 'foo'),
                         fill_empty_values(self.df, 'km', 'foo'))
        self.assertRaises(TypeError, exec_function, 'made_out_function', self.df, 'param1')

    def test_birthdate_to_age(self):
        birthdate_to_age(self.df, 'user_birthdate', 'age')
        self.assertEqual(self.df['age'][0], calculate_age(self.df['user_birthdate'][0]))
        self.assertEqual(self.df['age'][3], calculate_age(self.df['user_birthdate'][3]))
        self.assertEqual(self.df['age'][5], calculate_age(self.df['user_birthdate'][5]))

    def test_hot_encoding(self):
        hot_encoding(self.df, 'vehicle_category')
        self.assertEqual(self.df['is_small'][0], 1)
        self.assertEqual(self.df['is_small'][4], 0)
        self.assertEqual(self.df['is_small'][12], 0)
        self.assertEqual(self.df['is_medium'][0], 0)
        self.assertEqual(self.df['is_medium'][4], 1)
        self.assertEqual(self.df['is_medium'][12], 0)
        self.assertEqual(self.df['is_large'][0], 0)
        self.assertEqual(self.df['is_large'][4], 0)
        self.assertEqual(self.df['is_large'][12], 1)

    def test_fill_empty_values(self):
        fill_empty_values(self.df, 'km', 'foo_km')
        fill_empty_values(self.df, 'user_name', 'foo_user')
        self.assertFalse(self.df['km'].isnull().any())
        self.assertFalse(self.df['user_name'].isnull().any())
