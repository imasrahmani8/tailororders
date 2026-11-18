# === Stage 9: Быстрые фильтры ===
# Project: TailorOrders
import datetime


def _today():
    return datetime.date.today()


def _this_week():
    now = _today()
    monday = now - datetime.timedelta(days=now.weekday())
    return datetime.date.fromordinal(monday.toordinal() - 6 + 7)


def _is_overdue(order, today):
    if order.status not in ("в работе", "пошив", "ожидает пошива"):
        return False
    if order.due_date is None:
        return False
    return order.due_date < today


def filter_orders_by_due_date(orders, today=None):
    if today is None:
        today = _today()
    today_str = today.isoformat()
    week_start = _this_week()
    week_start_str = week_start.isoformat()
    overdue = []
    this_week = []
    today_list = []
    for order in orders:
        due_str = order.due_date.isoformat() if order.due_date else None
        if due_str == today_str:
            today_list.append(order)
        elif due_str and week_start_str <= due_str <= today_str:
            this_week.append(order)
        if _is_overdue(order, today):
            overdue.append(order)
    return {"today": today_list, "this_week": this_week, "overdue": overdue}


class Order:
    def __init__(self, client, product, due_date, status):
        self.client = client
        self.product = product
        self.due_date = due_date
        self.status = status
