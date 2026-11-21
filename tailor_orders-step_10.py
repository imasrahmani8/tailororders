# === Stage 10: Поиск дубликатов ===
# Project: TailorOrders
import hashlib
from typing import Dict, List, Optional, Tuple


def normalize_client(name: Optional[str]) -> str:
    if name is None:
        return ""
    text = name.strip().lower()
    return " ".join(text.split())


def normalize_product(product: Optional[str]) -> str:
    if product is None:
        return ""
    text = product.strip().lower()
    return " ".join(text.split())


def normalize_deadline(deadline: Optional[str]) -> str:
    if deadline is None:
        return ""
    text = str(deadline).strip().lower()
    return " ".join(text.split())


def signature(order: dict) -> str:
    client = normalize_client(order.get("client"))
    product = normalize_product(order.get("product"))
    deadline = normalize_deadline(order.get("deadline"))
    raw = f"{client}|{product}|{deadline}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def find_duplicates(orders: List[dict]) -> List[Tuple[dict, ...]]:
    groups: Dict[str, List[dict]] = {}
    for order in orders:
        key = signature(order)
        groups.setdefault(key, []).append(order)
    return [group for group in groups.values() if len(group) > 1]
