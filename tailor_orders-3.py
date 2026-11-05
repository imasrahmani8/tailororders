# === Stage 3: Хранилище в памяти ===
# Project: TailorOrders
memory_store.py

from datetime import datetime


class Order:
    def __init__(self, order_id, client, garment, deadline, status="new"):
        self.order_id = order_id
        self.client = client
        self.garment = garment
        self.deadline = deadline
        self.status = status

    def __repr__(self):
        return (
            f"Order(id={self.order_id}, client={self.client!r}, "
            f"garment={self.garment!r}, deadline={self.deadline}, "
            f"status={self.status!r})"
        )


class MemoryOrderStore:
    def __init__(self):
        self._orders = {}

    def add_order(self, order):
        if not order.order_id:
            raise ValueError("order_id must be provided")
        self._orders[order.order_id] = order
        return order

    def get_order(self, order_id):
        return self._orders.get(order_id)

    def list_orders(self, status=None):
        if status is None:
            return list(self._orders.values())
        return [o for o in self._orders.values() if o.status == status]

    def count(self):
        return len(self._orders)


def parse_deadline(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"invalid deadline format: {text!r}")


def create_order(order_id, client, garment, deadline):
    return Order(order_id, client, garment, parse_deadline(deadline))
