# Thoughts: keep each type of discount (n for m limit p, n for $y, reduced price, etc)
#       discountType1 -> Product 1
#                     -> Proudct 2
#
#       discountType2 -> Product 1
#                     -> Proudct 2

# ie 2 for 1, limit <none>
#    2 get 1 half off
#    n = required items(total items)
#    m = discounted items(total items - full price = this)
#    y = discount % of m items ( price * y = discounted price )
#    z = limit ( 0 = no limit)
n_for_m_limit_y = {"Gum": [2, 1, 0, 1]}


def discount_engine(cart):
    for d_item, discount in n_for_m_limit_y.iteritems():
        for c_item, item in cart:
            if d_item == c_item:
                if cart[d_item] >= n_for_m_limit_y[d_item][0]:
                    cart.discounts[]