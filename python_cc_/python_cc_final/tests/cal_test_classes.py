import unittest
from backEnd.classes import Order


class OrderMakingTestCase(unittest.TestCase):

    def test_order_id_generation(self):
        current_counter = Order.counter

        order1 = Order([])
        expected_order_id = f"order-{current_counter}"
        self.assertEqual(order1.order_id, expected_order_id)

        order2 = Order([])
        new_expected_order_id = f"order-{current_counter + 1}"
        self.assertEqual(order2.order_id, new_expected_order_id)
