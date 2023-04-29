from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    salaries = set(map(lambda salary: int(salary["max_salary"]) if (
        salary["max_salary"].isdigit())
        else 0, jobs))
    # print(max(salaries) if salaries else 0)
    return max(salaries) if salaries else 0


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    salaries = set(map(lambda salary: int(salary["min_salary"]) if (
        salary["min_salary"].isdigit())
        else 999999, jobs))
    # print(min(salaries))
    return min(salaries) if salaries else 0


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    -------
    referência https://www.youtube.com/watch?v=xz2B3bfNjEk
    """
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        is_it_true = min_salary > max_salary
        salary_in_int = int(salary)

    # except Exception as error:
    #     print(f'oi {error.__class__} oi')
    except (KeyError, TypeError):
        raise ValueError("Wrong value of salaries")
    if is_it_true:
        raise ValueError("Min salary is grather than Max salary")
    return (min_salary).__le__(salary_in_int) and (
        max_salary).__ge__(salary_in_int)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    salary_filtered = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_filtered.append(job)
        except ValueError:
            continue
    return salary_filtered
