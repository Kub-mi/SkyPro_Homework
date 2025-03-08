# Проект по маскировке данных

Этот проект включает в себя несколько функций для маскировки личных данных, таких как номер банковской карты и номер счета, а также для вывода даты в заданном формате.

## Цель проекта

Цель проекта — предоставить простые и удобные функции для обработки и маскировки данных, что может быть полезно для обеспечения конфиденциальности в различных приложениях, таких как онлайн-банкинг или системы оплаты.

## Функции проекта

1. **mask_account_card** - Маскирует номера банковской карты и счета.
2. **get_date** - Преобразует дату в формат "ДД.ММ.ГГГГ".
3. **get_mask_card_number** - Маскирует номер карты, отображая его в формате ХХХ****XXXX.
4. **get_mask_account** - Маскирует номер счета, отображая его в формате **XXXX.

## Установка

Для использования этого проекта нужно:

1. Клонировать репозиторий:

   ```bash
   git@github.com:Kub-mi/SkyPro_Homework.git

# Тестирование функций обработки данных

## Описание
Этот проект содержит тесты для функций, выполняющих фильтрацию, сортировку и маскирование данных.

## Установка и запуск тестов

### Установка зависимостей
Перед запуском тестов убедитесь, что у вас установлен `pytest`. Если он не установлен, выполните команду:

```bash
pip install pytest
```

### Запуск тестов
Запустить тесты можно с помощью команды:

```bash
pytest
```

---

## Описание тестов

### 1. Тестирование функции `filter_by_state`
Функция `filter_by_state` фильтрует список операций по их состоянию (`state`).

#### Проверяемые случаи:
- Корректная фильтрация списка операций
- Обработка данных, в которых отсутствует ключ `state`
- Обработка данных, в которых `state` имеет некорректный тип

```python
def test_filter_by_state(exemple_processing, exemple_processing_no_state, exemple_processing_no_type):
    right_exemple_processing = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    rigth_exemple_processing_no_type = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

    assert filter_by_state(exemple_processing) == right_exemple_processing
    assert filter_by_state(exemple_processing_no_state) == {'state': 'Нет элементов'}
    assert filter_by_state(exemple_processing_no_type) == rigth_exemple_processing_no_type
```

---

### 2. Тестирование функции `sort_by_date`
Функция `sort_by_date` сортирует список операций по дате.

#### Проверяемые случаи:
- Сортировка по убыванию (по умолчанию)
- Сортировка по возрастанию

```python
def test_sort_by_date(exemple_processing):
    right_sort_true = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    right_sort_false = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(exemple_processing) == right_sort_true
    assert sort_by_date(exemple_processing, False) == right_sort_false
```

---

### 3. Тестирование функции `mask_account_card`
Функция `mask_account_card` маскирует номера карт и счетов.

#### Проверяемые случаи:
- Корректное маскирование номера карты
- Корректное маскирование номера счета
- Обработка некорректных данных (длина номера не соответствует требованиям)

```python
def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"

    with pytest.raises(ValueError):
        mask_account_card("1234")
```

---

### 4. Тестирование функции `get_date`
Функция `get_date` преобразует дату в формат `ДД.ММ.ГГГГ`.

#### Проверяемые случаи:
- Корректное преобразование даты
- Параметризованный тест с разными входными значениями

```python
def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-02-11T02:26:18.671407", "11.02.2024"),
        ("2025-03-11T02:26:18.671407", "11.03.2025"),
    ],
)
def test_get_date_param(value, expected):
    assert get_date(value) == expected
```

---

### 5. Тестирование функций маскировки номеров карт и счетов
Функции `get_mask_card_number` и `get_mask_account` маскируют номера карт и счетов.

#### Проверяемые случаи:
- Корректное маскирование номера карты
- Корректное маскирование номера счета
- Обработка некорректных номеров (неправильное количество цифр)

```python
def test_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"

    with pytest.raises(ValueError):
        get_mask_card_number("1234")

    with pytest.raises(ValueError):
        get_mask_card_number("123467890123456789")

def test_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account(12345678901234567890) == "**7890"

    with pytest.raises(ValueError):
        get_mask_account("1234")

    with pytest.raises(ValueError):
        get_mask_account("123456789012345678912345")
```

---

## Заключение
Этот набор тестов позволяет убедиться в корректной работе функций обработки данных. Если какой-либо тест не проходит, следует проверить логику работы соответствующей функции.

