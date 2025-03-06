from src.widget import get_date


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_by_state = []
    for item in data:
        if item.get("state") == state:
            filtered_by_state.append(item)
        else:
            filtered_by_state = "Нет элементов"
    return filtered_by_state


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует список словарей по значению ключа 'data'"""
    sorted_data = data[:]
    sorted_data.sort(key=lambda x: get_date(x["date"]), reverse=descending)
    return sorted_data
