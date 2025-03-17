from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(exemple_processing, exemple_processing_no_state, exemple_processing_no_type):
    right_exemple_processing = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    rigth_exemple_processing_no_type = [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

    assert filter_by_state(exemple_processing) == right_exemple_processing
    assert filter_by_state(exemple_processing_no_state) == [{"state": "Нет элементов"}]
    assert filter_by_state(exemple_processing_no_type) == rigth_exemple_processing_no_type


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
