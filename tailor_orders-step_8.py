# === Stage 8: Теги ===
# Project: TailorOrders
from typing import Dict, List, Optional


class Tag:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Tag) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Tag({self.name!r})"


class Order:
    def __init__(self, client: str, product: str, deadline: str, status: str):
        self.client = client
        self.product = product
        self.deadline = deadline
        self.status = status
        self.tags: Dict[str, Tag] = {}

    def add_tag(self, name: str) -> Tag:
        tag = Tag(name)
        self.tags[name] = tag
        return tag

    def remove_tag(self, name: str) -> bool:
        if name in self.tags:
            del self.tags[name]
            return True
        return False

    def get_tags(self) -> List[Tag]:
        return list(self.tags.values())

    def has_tag(self, name: str) -> bool:
        return name in self.tags


def find_orders_by_tag(orders: List[Order], tag_name: str) -> List[Order]:
    return [order for order in orders if order.has_tag(tag_name)]


if __name__ == "__main__":
    order = Order("Иванов", "Пальто", "2024-12-01", "пошив")
    order.add_tag("зимнее")
    order.add_tag("срочное")
    order.remove_tag("срочное")
    for tag in order.get_tags():
        print(tag)
    print(order.has_tag("зимнее"))
    print(find_orders_by_tag([order], "зимнее"))
