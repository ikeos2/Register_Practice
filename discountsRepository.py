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
#  [3]  z = limit ( 0 = no limit)
n_for_m_limit_y = {"Gum": [2, 1, 0, 1]}

