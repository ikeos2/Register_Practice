from unittest import TestCase
from Register import Register
from priceRepository import priceRepository

class TestRegister(TestCase):
    def test_scan_item(self):
        reg = Register()
        self.assertEqual(reg.scan_item("Ground Beef", 1), 3.99)

    # def test_get_total(self):
    #     self.fail()
