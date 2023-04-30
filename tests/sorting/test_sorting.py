from src.pre_built.sorting import sort_by


list_jobs = [
    {
        "min_salary": 1111,
        "max_salary": 2222,
        "date_posted": "2022-11-22"
    },
    {
        "min_salary": 2222,
        "max_salary": 3333,
        "date_posted": "2023-11-22"
    },
]


mock_max_salary = [
    {
        "min_salary": 2222,
        "max_salary": 3333,
        "date_posted": "2023-11-22"
    },
    {
        "min_salary": 1111,
        "max_salary": 2222,
        "date_posted": "2022-11-22"
    },
]


mock_min_salary = [
    {
        "min_salary": 1111,
        "max_salary": 2222,
        "date_posted": "2022-11-22"
    },
    {
        "min_salary": 2222,
        "max_salary": 3333,
        "date_posted": "2023-11-22"
    },
]


mock_date_posted = [
    {
        "min_salary": 2222,
        "max_salary": 3333,
        "date_posted": "2023-11-22"
    },
    {
        "min_salary": 1111,
        "max_salary": 2222,
        "date_posted": "2022-11-22"
    },
]


def test_sort_by_criteria():
    sort_by(list_jobs, 'max_salary')
    assert list_jobs == mock_max_salary
    sort_by(list_jobs, 'min_salary')
    assert list_jobs == mock_min_salary
    sort_by(list_jobs, 'date_posted')
    assert list_jobs == mock_date_posted
