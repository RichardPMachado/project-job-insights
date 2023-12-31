from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    list_of_unique_indutries = set([industries['industry'] for industries in
                                    jobs if (industries['industry'])])
    # print(list(list_of_unique_indutries))
    return list(list_of_unique_indutries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # print([job for job in jobs if (job["industry"] == industry)])
    return [job for job in jobs if (job["industry"] == industry)]
