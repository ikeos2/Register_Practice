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

    # def test_get_total(self):
    #     self.fail()
