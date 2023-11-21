import unittest
from backEnd.utils import calories_counter, comp_cal_counter, comp_cal_counter2
from backEnd.exceptions import BigMealException


class BigMealTestCase(unittest.TestCase):

    def assert_big_meal_exception(self, function, expected_message, *args):
        with self.assertRaises(BigMealException) as e:
            function(*args)
            self.assertEqual(
                e.exception.message,
                expected_message,
                "Wrong exception message"
            )

    def test_calories_counter_exception(self):
        expected_message = "Meal has 3210 calories, which is too much!"
        self.assert_big_meal_exception(calories_counter, expected_message, 'Cheesy Combo', 'Cheesy Combo', 'Cheesy Combo')

    def test_comp_cal_counter_exception(self):
        expected_message = "Meal has 3210 calories, which is too much!"
        self.assert_big_meal_exception(comp_cal_counter, expected_message, 'combo-1', 'combo-1', 'combo-1')

    def test_comp_cal_counter2_exception(self):
        expected_message = "Meal has 3210 calories, which is too much!"
        self.assert_big_meal_exception(comp_cal_counter2, expected_message, 'combo-1', 'combo-1', 'combo-1')
