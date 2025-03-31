from collections import defaultdict
from typing import Dict, List, Any


def count_of_category(transs: List[Dict[str, str]], categories: List[str]) -> defaultdict[Any, int]:
    """Подсчитывает количество операций в каждой категории"""
    category_count = defaultdict(int)
    for transaction in transs:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
                break
    return category_count
