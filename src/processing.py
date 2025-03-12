from src.widget import get_date


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_by_state = []

    for item in data:
        state_value = item.get("state")

        # Проверяем, что значение state является строкой
        if not isinstance(state_value, str):
            print(
                f"Ошибка: значение 'state' должно быть строкой, но получено "
                f"{type(state_value).__name__} ({state_value})"
            )
            continue
        if item.get("state") == state:
            filtered_by_state.append(item)

    return filtered_by_state if filtered_by_state else [{'state': 'Нет элементов'}]


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует список словарей по значению ключа 'data'"""
    sorted_data = data[:]
    sorted_data.sort(key=lambda x: get_date(x["date"]), reverse=descending)
    return sorted_data
