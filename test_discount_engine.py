from unittest import TestCase
from discountEngine import discount_engine, limit_y


class TestDiscount_engine(TestCase):
    def test_discount_engine_empty_cart(self):
        self.assertEqual(discount_engine({}), {})

    def test_discount_engine_one_item_cart_no_valid_discount(self):
        results = {'Ground Beef': 9999.99}
        self.assertEqual(results, discount_engine({"Ground Beef": 1}))

    def test_discount_engine_one_item_cart_with_valid_discount(self):
        results = {'Gum': .25}
        self.assertEqual(results, discount_engine({"Gum": 2}))

    def test_discount_engine_items_cart_with_valid_discount(self):
        results = {'Gum': .5}
        self.assertEqual(results, discount_engine({"Gum": 3}))

    def test_discount_engine_items_cart_with_valid_discount(self):
        results = discount_engine({"Gum": 4})
        self.assertEqual({'Gum': .75}, results)

    def test_ten_percent_off_discount(self):
        self.assertEqual({'Chicken Soup': 3.582}, discount_engine({"Chicken Soup": 2}))
        self.assertEqual({'Chicken Soup': 5.373}, discount_engine({"Chicken Soup": 3}))

    def test_multiple_valid_discounts(self):
        results = discount_engine({"Mustard": 3})
        self.assertEqual({'Mustard': 3.00}, results)

    def test_n_for_m_fixed(self):
        results = discount_engine({"Milk": 2})
        self.assertEqual({'Milk': 7.00}, results)

    def test_multiple_of_same_discount(self):
        results = discount_engine({"Coke": 6})
        self.assertEqual({'Coke': 6.00}, results)

    def test_weighted_item_n_for_m(self):
        results = discount_engine({"Ground Beef": 1.0, "Chicken": 1.0})
        self.assertEqual({"Ground Beef": 9999.99, "Chicken": 2.70}, results)  # Ground beef wont have a discount, but chicken will

    def test_no_discounts(self):
        results = discount_engine({"Bread": 1.0})
        self.assertEqual({"Bread": 9999.99}, results)


class TestLimitY(TestCase):
    def test_limit_given_lower_than_limit(self):
        self.assertEqual(limit_y(1, 2), 1)

    def test_limit_given_higher_than_limit(self):
        self.assertEqual(limit_y(3, 2), 2)

    def test_limit_given_no_limit(self):
        self.assertEqual(limit_y(10, 0), 10)
