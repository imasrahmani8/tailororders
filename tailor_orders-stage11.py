# === Stage 11: Массовое обновление ===
# Project: TailorOrders
from __future__ import annotations


class Order:
    def __init__(self, client: str, item: str, due_date: str, status: str) -> None:
        self.client = client
        self.item = item
        self.due_date = due_date
        self.status = status

    def __repr__(self) -> str:
        return f"Order(client={self.client!r}, item={self.item!r}, " \
               f"due_date={self.due_date!r}, status={self.status!r})"


class Fitting:
    def __init__(self, order: Order, date: str, notes: str) -> None:
        self.order = order
        self.date = date
        self.notes = notes

    def __repr__(self) -> str:
        return f"Fitting(order={self.order!r}, date={self.date!r}, notes={self.notes!r})"


class TailorOrders:
    def __init__(self) -> None:
        self.orders: dict[str, Order] = {}

    def add_order(self, order: Order) -> None:
        self.orders[order.client] = order

    def apply_changes(self, predicate, changes, clients=None) -> list[Order]:
        if clients is None:
            clients = list(self.orders.keys())
        updated: list[Order] = []
        for client in clients:
            order = self.orders.get(client)
            if order is None:
                continue
            if predicate(order):
                for key, value in changes.items():
                    setattr(order, key, value)
                updated.append(order)
        return updated

    def preview_changes(self, predicate, changes, clients=None) -> list[tuple[Order, dict]]:
        if clients is None:
            clients = list(self.orders.keys())
        preview: list[tuple[Order, dict]] = []
        for client in clients:
            order = self.orders.get(client)
            if order is None:
                continue
            if predicate(order):
                modified = {key: changes[key]
                            for key in changes if key in order.__dict__}
                preview.append((order, modified))
        return preview


if __name__ == "__main__":
    shop = TailorOrders()
    shop.add_order(Order("Иванов", "Пальто", "2026-01-10", "в работе"))
    shop.add_order(Order("Петрова", "Платье", "2026-01-05", "в работе"))
    shop.add_order(Order("Сидоров", "Костюм", "2026-02-01", "готов"))

    predicate = lambda order: order.status == "в работе"
    changes = {"status": "на примерке"}

    print("Предварительный просмотр изменений:")
    for order, modified in shop.preview_changes(predicate, changes):
        print(f"  {order} -> {modified}")

    print("\nПрименяю изменения:")
    for order in shop.apply_changes(predicate, changes):
        print(f"  {order}")
