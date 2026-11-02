# === Stage 1: Каркас модуля ===
# Project: TailorOrders
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Order:
    client: str
    item: str
    deadline: date
    status: str = "new"


def make_demo_orders() -> list:
    return [
        Order("Иванов И.И.", "Пальто", date(2024, 6, 15), "new"),
        Order("Петрова А.С.", "Платье", date(2024, 6, 20), "new"),
        Order("Сидоров К.В.", "Костюм", date(2024, 7, 1), "new"),
    ]


def main() -> None:
    orders = make_demo_orders()
    print("Тестовые заказы ателье:")
    for order in orders:
        print(f"  {order.client} — {order.item}, срок: {order.deadline}, статус: {order.status}")


if __name__ == "__main__":
    main()
