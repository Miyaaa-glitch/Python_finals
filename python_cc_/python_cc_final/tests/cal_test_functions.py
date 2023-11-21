import unittest
from backEnd.utils import calories_counter
from backEnd.jsonUtils import comp_cal_counter_json, price_counter_json

class CalorieCounterTestCase(unittest.TestCase):

    def test_calories_simple(self):
        self.assertEqual(calories_counter('Hamburger', 'Salad', 'Iced Tea'), 685)

    def test_calories_combo(self):
        self.assertEqual(calories_counter('Cheesy Combo'), 1070)

    def test_mix(self):
        self.assertEqual(calories_counter('Hamburger', 'Cheesy Combo'), 1670)


class JsonFileTestCase(unittest.TestCase):

    def test_json_calories_combo_complex_id(self):
        self.assertEqual(comp_cal_counter_json('combo-1', 'combo-2'), 1770)

    def test_json_calories_combo_complex_name(self):
        self.assertEqual(comp_cal_counter_json('cheesy combo', 'veggie combo'), 1770)

    def test_json_calories_complex_mix_id(self):
        self.assertEqual(comp_cal_counter_json('meal-1', 'combo-2'), 1300)

    def test_json_calories_complex_mix_name(self):
        self.assertEqual(comp_cal_counter_json('hamburger', 'veggie combo'), 1300)


class PriceCounterTestCase(unittest.TestCase):

    def test_price_complex_id(self):
        self.assertEqual(price_counter('meal-1', 'meal-2', 'meal-3'), 18)

    def test_price_complex_name(self):
        self.assertEqual(price_counter('hamburger', 'salad', 'iced tea'), 11)
