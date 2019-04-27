# Thoughts: keep each type of discount (n for m limit p, n for $y, reduced price, etc)
#       discountType1 -> Product 1
#                     -> Proudct 2
#
#       discountType2 -> Product 1
#                     -> Proudct 2

# ie 2 for 1, limit <none>
#    2 get 1 half off
#  [0]  n = required items(total items)
#  [1]  m = discounted items(total items - full price = this)
#  [2]  y = discount % of m items ( price * y = discounted price )
#  [3]  z = limit of discounted items ( 0 = no limit)
n_for_m_limit_y = {"Gum": [2, 1, 0.00, 1],  # Buy 2 get 1 free
                   "Chicken Soup": [1, 1, .9, 0]}  # 10% off


# ie 2 for 1, limit <none>
#    2 get 1 half off
#  [0]  n = required items(total items)
#  [1]  m = total price for n items
#  [2]  z = limit ( 0 = no limit)
n_for_m__limit_y_fixed = {"Milk": [2, 7.00, 2]}
