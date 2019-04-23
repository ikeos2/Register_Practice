from priceRepository import priceRepository


class Register:
    def __init__(self):
        self.cart = {}
        self.total = 0.00

    def scan_item(self, item, units):
        ret = 0.00
        if item in priceRepository:
            if item not in self.cart:
                self.cart[item] = units
            else:
                self.cart[item] += units
            ret = priceRepository[item] * units  # show the price of the thing we just scanned @ # of units
        self.total += ret
        return ret

    def get_total(self):
        return self.total


if __name__ == "__main__":
    reg = Register()
    print(reg.scan_item("Ground Beef", 1))
    print(reg.get_total())
