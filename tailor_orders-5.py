# === Stage 5: Генерация идентификаторов ===
# Project: TailorOrders
import uuid


PROJECT_PREFIX = "tailor"


class DuplicateIdError(Exception):
    """Идентификатор уже существует в системе заказов."""


def generate_order_id(existing_ids):
    """Генерирует уникальный идентификатор заказа.

    Формат: {префикс}-{уникальный_сегмент}.
    Сегмент берётся из uuid4, преобразуется в строку и обрезаётся до 8 символов.
    Проверяется на коллизии с уже существующими идентификаторами.

    Args:
        existing_ids (set or list): множество или список уже занятых идентификаторов.

    Returns:
        str: уникальный идентификатор заказа.

    Raises:
        DuplicateIdError: если не удалось подобрать свободный идентификатор.
    """
    candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex[:8]}"
    if candidate in existing_ids:
        raise DuplicateIdError(f"Идентификатор {candidate} уже занят.")
    return candidate


def assign_order_id(existing_ids):
    """Удобная обёртка для генерации id с проверкой коллизий.

    Возвращает новый уникальный идентификатор заказа.

    Args:
        existing_ids (set or list): уже занятые идентификаторы.

    Returns:
        str: сгенерированный уникальный идентификатор заказа.
    """
    return generate_order_id(existing_ids)
