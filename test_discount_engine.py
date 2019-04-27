from unittest import TestCase
from discountEngine import discount_engine


class TestDiscount_engine(TestCase):
    def test_discount_engine_empty_cart(self):
        self.assertEqual(discount_engine({}), {})

    def test_discount_engine_one_item_cart_no_valid_discount(self):
        self.assertEqual(discount_engine({"Ground Beef": 1}), {'Ground Beef': 9999.99})

    def test_discount_engine_one_item_cart_with_valid_discount(self):
        self.assertEqual(discount_engine({"Gum": 2}), {'Gum': .25})


