from unittest import TestCase
from discountEngine import discount_engine, limit_y


class TestDiscount_engine(TestCase):
    def test_discount_engine_empty_cart(self):
        self.assertEqual(discount_engine({}), {})

    def test_discount_engine_one_item_cart_no_valid_discount(self):
        self.assertEqual(discount_engine({"Ground Beef": 1}), {'Ground Beef': 9999.99})

    def test_discount_engine_one_item_cart_with_valid_discount(self):
        self.assertEqual(discount_engine({"Gum": 2}), {'Gum': .25})

    def test_discount_engine_items_cart_with_valid_discount(self):
        self.assertEqual(discount_engine({"Gum": 3}), {'Gum': .5})

    def test_discount_engine_items_cart_with_valid_discount(self):
        self.assertEqual(discount_engine({"Gum": 4}), {'Gum': .75})

    def test_ten_percent_off_discount(self):
        self.assertEqual(discount_engine({"Chicken Soup": 2}), {'Chicken Soup': 3.582})
        self.assertEqual(discount_engine({"Chicken Soup": 3}), {'Chicken Soup': 5.373})

    def test_multiple_valid_discounts(self):
        self.assertEqual(discount_engine({"Mustard": 3}), {'Mustard': 3.00})

    def test_n_for_m_fixed(self):
        self.assertEqual(discount_engine({"Milk": 2}), {'Milk': 7.00})

class TestLimitY(TestCase):
    def test_limit_given_lower_than_limit(self):
        self.assertEqual(limit_y(1, 2), 1)

    def test_limit_given_higher_than_limit(self):
        self.assertEqual(limit_y(3, 2), 2)

    def test_limit_given_no_limit(self):
        self.assertEqual(limit_y(10, 0), 10)
