import unittest
from unittest import TestCase
from Register import Register


class TestRegister(TestCase):
    def setUp(self):
        self.reg = Register()

    def test_initial_register_state(self):
        self.assertEqual(self.reg.get_total(), 0.00)

    def test_scan_item_ground_beef(self):
        self.assertEqual(self.reg.scan_item("Ground Beef", 1), 3.99)

    def test_scan_item_milk(self):
        self.assertEqual(self.reg.scan_item("Milk", 1), 4.99)

    def test_scan_unknown_item(self):
        self.assertEqual(self.reg.scan_item("Mystery Goo", 10), 0.00)

    def test_scan_multiple_items(self):
        self.assertEqual(self.reg.scan_item("Milk", 1), 4.99)
        self.assertEqual(self.reg.scan_item("Ground Beef", 1), 3.99)

    def test_get_initial_total(self):
        self.assertEqual(self.reg.get_total(), 0.00)

    def test_get_total_with_item(self):
        self.reg.scan_item("Milk", 1)
        self.assertEqual(self.reg.get_total(), 4.99)

    def test_scan_and_total_multiple_items(self):
        self.assertEqual(self.reg.scan_item("Milk", 1), 4.99)
        self.assertEqual(self.reg.scan_item("Ground Beef", 1), 3.99)
        self.assertEqual(self.reg.get_total(), 8.98)

    def test_gum_2_for_1(self):
        self.reg.scan_item("Gum", 2)
        self.assertEqual(self.reg.get_total(), .25)

    def test_void_an_item(self):
        self.reg.scan_item("Milk", 1)
        self.reg.void_item("Milk", 1)
        self.assertEqual(self.reg.get_total(), 0.00)

    def test_void_an_item_with_one_leftover(self):
        self.reg.scan_item("Milk", 2)
        self.reg.void_item("Milk", 1)
        self.assertEqual(self.reg.get_total(), 4.99)

    def test_total_is_calculated_right_after_removing_special_item1(self):
        self.reg.scan_item("Gum", 3)
        self.reg.void_item("Gum", 1)
        self.assertEqual(self.reg.get_total(), .25)

    def test_total_is_calculated_right_after_removing_special_item2(self):
        self.reg.scan_item("Gum", 3)
        self.reg.void_item("Gum", 2)
        self.assertEqual(self.reg.get_total(), .25)


if __name__ == '__main__':
    unittest.main()

