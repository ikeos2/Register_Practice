from priceRepository import priceRepository


class Register:
    def scan_item(self, item, units):
        return priceRepository[item] * units

    def get_total(self):
        return 0.00


if __name__ == "__main__":
    reg = Register()
    reg.scan_item("Ground Beef", 1)
    reg.get_total()
