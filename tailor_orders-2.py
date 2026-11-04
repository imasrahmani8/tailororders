# === Stage 2: Проверка полей ===
# Project: TailorOrders
from datetime import datetime, date


def normalize_client(value):
    value = value.strip()
    if not value:
        raise ValueError("Клиент обязательно должен быть указан")
    parts = value.split()
    if len(parts) < 2:
        raise ValueError("Укажите имя и фамилию клиента")
    return value


def normalize_item(value):
    value = value.strip()
    if not value:
        raise ValueError("Изделие обязательно должно быть указано")
    if len(value) < 2:
        raise ValueError("Название изделия слишком короткое")
    valid = ("Пальто", "Платье", "Костюм", "Куртка", "Юбка", "Рубашка", "Брюки", "Пиджак")
    if value not in valid:
        raise ValueError("Неизвестное изделие, выберите из списка")
    return value


def normalize_deadline(value):
    if value is None:
        raise ValueError("Срок сдачи заказа обязателен")
    value = value.strip()
    if value and value not in ("срочно", "приоритет"):
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            if parsed.date() <= date.today():
                raise ValueError("Срок сдачи заказа уже наступил")
            return parsed.date()
        except ValueError:
            raise ValueError("Укажите корректную дату в формате ГГГГ-ММ-ДД")
    return value


def normalize_status(value):
    value = value.strip().lower()
    if value in ("в работе", "готово", "готов", "ожидаем", "ожидает", "отменён", "отменен", "отмена"):
        return value
    raise ValueError("Неверный статус, используйте один из вариантов")


def validate_order(order):
    errors = []
    if not order.get("client"):
        errors.append("Клиент обязателен")
    if not order.get("item"):
        errors.append("Изделие обязательно")
    if not order.get("deadline"):
        errors.append("Срок сдачи заказа обязателен")
    if not order.get("status"):
        errors.append("Статус заказа обязателен")
    return errors
