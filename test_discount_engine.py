from unittest import TestCase
from discountEngine import discount_engine


class TestDiscount_engine(TestCase):
    def test_discount_engine_empty_cart(self):
        self.assertEqual(discount_engine({}), {})

    def test_discount_engine_one_item_cart(self):
        self.assertEqual(discount_engine({"Ground Beef": 3.99}), {})
