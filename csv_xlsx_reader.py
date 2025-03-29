import csv

import pandas as pd


def csv_reader(file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            dict_trans = list(reader)
        return dict_trans
    except Exception as ex:
        print(f"Ошибка при чтении файла: {ex}")
        return []


def exel_reader(file_path: str) -> list:
    """Считывает финансовые операции из XLSX-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path, dtype=str, engine='openpyxl')
        trans_excel = df.to_dict(orient='records')
        return trans_excel
    except UnicodeDecodeError as ex:
        print(f"Ошибка кодировки: {ex}")
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
