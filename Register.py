from priceRepository import priceRepository
from discountEngine import discount_engine


class Register:
    def __init__(self):
        self.cart = {}
        self.discounts = {}

    def scan_item(self, item, units):
        ret = 0.00
        if item in priceRepository:
            if item not in self.cart:
                self.cart[item] = units
            else:
                self.cart[item] += units
            ret = priceRepository[item] * units  # show the price of the thing we just scanned @ # of units
        return ret

    def void_item(self, item, units):
        return

    def get_total(self):
        discounted_prices = discount_engine(self.cart)
        total = 0.00
        for item, units in self.cart.items():
            regular_price = priceRepository[item] * units
            discount_price = discounted_prices[item]
            total += min(regular_price, discount_price)
        return total


if __name__ == "__main__":
    reg = Register()
    print(reg.scan_item("Ground Beef", 1))
    print(reg.get_total())
