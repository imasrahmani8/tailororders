# === Stage 12: Избранное ===
# Project: TailorOrders
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Order:
    client: str
    garment: str
    deadline: str
    status: str = "новый"
    is_favorite: bool = False


class TailorOrders:
    def __init__(self):
        self.orders: List[Order] = []

    def add_order(self, client: str, garment: str, deadline: str) -> Order:
        order = Order(client=client, garment=garment, deadline=deadline)
        self.orders.append(order)
        return order

    def get_order(self, index: int) -> Optional[Order]:
        if 0 <= index < len(self.orders):
            return self.orders[index]
        return None

    def add_favorite(self, index: int) -> bool:
        order = self.get_order(index)
        if order is not None:
            order.is_favorite = True
            return True
        return False

    def remove_favorite(self, index: int) -> bool:
        order = self.get_order(index)
        if order is not None:
            order.is_favorite = False
            return True
        return False

    def is_favorite(self, index: int) -> bool:
        order = self.get_order(index)
        return order.is_favorite if order is not None else False

    def get_favorite_orders(self) -> List[Order]:
        return [order for order in self.orders if order.is_favorite]
