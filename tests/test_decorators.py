import pytest
import os

from decorators import log


# Тестируем правильный вывод в консоль
def test_log_success(capsys):
    @log()
    def test_func(a, b):
        return a + b

    test_func(3, 4)

    # Проверяем, что вывод в консоль соответствует ожидаемому
    captured = capsys.readouterr()
    assert captured.out.strip() == "test_func ok"


# Тестируем вывод в консоль при ошибке
def test_log_error(capsys):
    @log()
    def test_func(a, b):
        return a / b  # Деление на ноль вызывает ошибку

    try:
        test_func(3, 0)
    except ZeroDivisionError:
        pass

    # Проверяем, что ошибка корректно выводится в консоль
    captured = capsys.readouterr()
    assert "test_func error: ZeroDivisionError" in captured.out
    assert "Inputs: (3, 0), {}" in captured.out


# Тестируем запись в файл при успешном выполнении
def test_log_success_to_file():
    filename = "test_log.txt"

    @log(filename=filename)
    def test_func(a, b):
        return a + b

    test_func(5, 6)

    # Проверяем, что файл существует и содержит правильное сообщение
    with open(filename, "r") as file:
        content = file.read().strip()
        assert content == "test_func ok"

    # Удаляем временный файл
    os.remove(filename)


# Тестируем запись в файл при ошибке
def test_log_error_to_file():
    filename = "test_log.txt"

    @log(filename=filename)
    def test_func(a, b):
        return a / b  # Деление на ноль вызывает ошибку

    try:
        test_func(3, 0)
    except ZeroDivisionError:
        pass

    # Проверяем, что файл существует и содержит правильное сообщение об ошибке
    with open(filename, "r") as file:
        content = file.read().strip()
        assert "test_func error: ZeroDivisionError" in content
        assert "Inputs: (3, 0), {}" in content

    # Удаляем временный файл
    os.remove(filename)


# Тестируем использование декоратора без имени файла
def test_log_without_filename(capsys):
    @log()
    def test_func(a, b):
        return a + b

    test_func(1, 2)

    # Проверяем, что вывод в консоль соответствует ожидаемому
    captured = capsys.readouterr()
    assert captured.out.strip() == "test_func ok"


# Тестируем использование декоратора с ошибкой без имени файла
def test_log_error_without_filename(capsys):
    @log()
    def test_func(a, b):
        return a / b  # Деление на ноль вызывает ошибку

    try:
        test_func(1, 0)
    except ZeroDivisionError:
        pass

    # Проверяем, что ошибка корректно выводится в консоль
    captured = capsys.readouterr()
    assert "test_func error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out
