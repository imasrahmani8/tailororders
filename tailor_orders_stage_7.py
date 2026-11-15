# === Stage 7: Поиск по нескольким словам ===
# Project: TailorOrders
from typing import List, Set


class OrderSearchException(Exception):
    pass


def search_orders(orders: List[dict], query: str) -> List[dict]:
    terms: Set[str] = set()
    exclusions: Set[str] = set()

    for token in query.split():
        if token.startswith("-"):
            exclusions.add(token[1:].lower())
        else:
            terms.add(token.lower())

    results: List[dict] = []

    for order in orders:
        text = " ".join(
            str(value).lower()
            for value in order.values()
            if not isinstance(value, (list, dict))
        )

        if not terms and not exclusions:
            results.append(order)
            continue

        matches_all = True
        for term in terms:
            if term not in text:
                matches_all = False
                break

        matches_any = any(exclusion in text for exclusion in exclusions)

        if matches_all and not matches_any:
            results.append(order)

    return results


if __name__ == "__main__":
    sample_orders = [
        {
            "client": "Иванов",
            "product": "Пальто",
            "deadline": "2024-12-31",
            "status": "В работе",
        },
        {
            "client": "Петров",
            "product": "Костюм",
            "deadline": "2024-11-15",
            "status": "Готов",
        },
        {
            "client": "Сидоров",
            "product": "Платье",
            "deadline": "2025-01-10",
            "status": "В работе",
        },
    ]

    print(search_orders(sample_orders, "пальто готов"))
    print(search_orders(sample_orders, "пальто -готов"))
    print(search_orders(sample_orders, "сидоров костюм"))
