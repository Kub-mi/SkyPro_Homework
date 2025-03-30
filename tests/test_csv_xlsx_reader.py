from unittest.mock import patch, mock_open

import pandas as pd

from csv_xlsx_reader import csv_reader, excel_reader


@patch("builtins.open", new_callable=mock_open,
       read_data="date;amount;category\n2024-01-01;100;Food\n2024-01-02;200;Transport\n")
@patch("csv.DictReader")
def test_csv_reader(mock_dict_reader, mock_file):
    mock_dict_reader.return_value = [
        {"date": "2024-01-01", "amount": "100", "category": "Food"},
        {"date": "2024-01-02", "amount": "200", "category": "Transport"}
    ]

    result = csv_reader("fake_path.csv")
    assert len(result) == 2
    assert result[0]["date"] == "2024-01-01"
    assert result[1]["category"] == "Transport"
    mock_file.assert_called_once_with("fake_path.csv", mode="r", encoding="utf-8")


@patch("pandas.read_excel")
def test_excel_reader(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([
        {"date": "2024-01-01", "amount": "150", "category": "Shopping"},
        {"date": "2024-01-03", "amount": "300", "category": "Rent"}
    ])

    result = excel_reader("fake_path.xlsx")
    assert len(result) == 2
    assert result[0]["date"] == "2024-01-01"
    assert result[1]["amount"] == "300"
    mock_read_excel.assert_called_once_with("fake_path.xlsx", dtype=str, engine='openpyxl')
