# === Stage 4: Связи между сущностями ===
# Project: TailorOrders
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterator


@dataclass(frozen=True)
class Client:
    name: str
    phone: str


@dataclass(frozen=True)
class Product:
    kind: str
    size: str


@dataclass
class Order:
    client: Client
    product: Product
    due_date: date
    status: str = "new"

    def __hash__(self) -> int:
        return hash((self.client, self.product, self.due_date, self.status))


@dataclass
class Fitting:
    order: Order
    date: date
    notes: str = ""


class OrderRepository:
    def __init__(self, orders: list[Order] | None = None) -> None:
        self._orders: list[Order] = list(orders) if orders else []

    def add_order(self, order: Order) -> None:
        if order not in self._orders:
            self._orders.append(order)

    def orders(self) -> list[Order]:
        return list(self._orders)


def iter_fittings(order: Order) -> Iterator[Fitting]:
    if order is None:
        return
    for fitting in order.order_fittings:
        yield fitting


class OrderModel:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def fittings(self, order: Order) -> list[Fitting]:
        return list(iter_fittings(order))

    def check_integrity(self, order: Order) -> bool:
        if order is None:
            return False
        for fitting in self.fittings(order):
            if fitting.order is not order:
                return False
        return True


def build_sample() -> tuple[OrderModel, Order]:
    repo = OrderRepository()
    client = Client(name="Иванов Иван", phone="+7 (900) 000-00-00")
    product = Product(kind="пиджак", size="48")
    order = Order(client=client, product=product, due_date=date(2025, 1, 10))
    repo.add_order(order)
    model = OrderModel(repo)
    fitting = Fitting(order=order, date=date(2025, 1, 5), notes="проверить плечо")
    order.order_fittings = [fitting]
    return model, order


if __name__ == "__main__":
    model, order = build_sample()
    print("примерки:", model.fittings(order))
    print("целостность:", model.check_integrity(order))
