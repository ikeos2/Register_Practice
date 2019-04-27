from priceRepository import priceRepository
from discountsRepository import n_for_m_limit_y, n_for_m_limit_y_fixed


def limit_y(num_items, max_items):
    if max_items == 0:
        return num_items
    if num_items > max_items:
        return max_items
    return num_items


def discount_engine(cart):
    discounts = {}
    for c_item, c_units in cart.items():  # For every item in our cart
        discounts[c_item] = {}  # Create a list of all the discounts available for this
        if c_item in n_for_m_limit_y:
            discounts[c_item]['n_for_m_limit_y'] = 9999.99  # if there is a discount available for item of this type
            if c_units >= n_for_m_limit_y[c_item][0]:  # if we have enough items to qualify for the discount
                item_limit = limit_y(c_units, n_for_m_limit_y[c_item][3])  # get max number of discounted items
                regular_price = priceRepository[c_item]  # Item's regular price
                # now set the discounted price
                discounts[c_item]['n_for_m_limit_y'] = item_limit * regular_price * n_for_m_limit_y[c_item][2] \
                                                       + (c_units - item_limit) * regular_price
        if c_item in n_for_m_limit_y_fixed:
            discounts[c_item]['n_for_m_limit_y_fixed'] = 9999.99  # if there is a discount available for item of this type
            if c_units >= n_for_m_limit_y_fixed[c_item][0]:  # if we have enough items to qualify for the discount
                item_limit = limit_y(c_units, n_for_m_limit_y_fixed[c_item][2])  # get max number of discounted items
                regular_price = priceRepository[c_item]  # Item's regular price
                fixed_price = n_for_m_limit_y_fixed[c_item][1]
                # now set the discounted price
                discounts[c_item]['n_for_m_limit_y_fixed'] = fixed_price + \
                                                             (max(c_units - item_limit, 0.0) * regular_price)

    # set discounts_return[item] to reflect lowest price
    lowest_discounts = {}
    for item, discount_types_dict in discounts.items():
        min_price = 9999.99  # Find the lowest price given all discounts
        for discount_type, price in discount_types_dict.items():
            if min_price > price:
                min_price = price
        lowest_discounts[item] = min_price
    # return dict of lowest totals
    return lowest_discounts
