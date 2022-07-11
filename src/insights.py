from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    list_of_unique_job_types = set()
    for job in jobs_list:
        list_of_unique_job_types.add(job["job_type"])
    return list_of_unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_list = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_list.append(job)
    return filtered_list


def get_unique_industries(path):
    jobs_list = read(path)
    list_of_unique_industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            list_of_unique_industries.add(job["industry"])
    return list_of_unique_industries


def filter_by_industry(jobs, industry):
    filtered_list = list()
    for job in jobs:
        if job["industry"] == industry:
            filtered_list.append(job)
    return filtered_list


def get_max_salary(path):
    jobs_list = read(path)
    salaries = list()
    for job in jobs_list:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    max_salary = max(salaries)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    salaries = list()
    for job in jobs_list:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    min_salary = min(salaries)
    return min_salary


def matches_salary_range(job, salary):
    """
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        if int(job["min_salary"]) < 0 or int(job["max_salary"]) < 0:
            raise ValueError()
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError()
        return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])
    except (TypeError, KeyError):
        raise ValueError()


def filter_by_salary_range(jobs, salary):
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
    return []
