import re
from typing import List, Dict


def filter_by_description(transactions: List[Dict[str, str]], search_query: str) -> List[Dict[str, str]]:
    """Фильтрует список банковских операций по строке поиска в описании"""
    pattern = re.compile(re.escape(search_query), re.IGNORECASE)
    result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]
    return result

def count_of_category():
    pass