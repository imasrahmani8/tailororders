# === Stage 6: Фильтрация записей ===
# Project: TailorOrders
def filter_orders_by_product(orders, product, start_date=None, end_date=None):
    filtered = []
    for order in orders:
        if order.get('product') != product:
            continue
        order_date = order.get('date')
        if start_date and order_date < start_date:
            continue
        if end_date and order_date > end_date:
            continue
        filtered.append(order)
    return filtered


def filter_orders_by_product_and_date_range(orders, product, start_date=None, end_date=None):
    return filter_orders_by_product(orders, product, start_date, end_date)
