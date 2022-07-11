import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_data = csv.DictReader(file, delimiter=",", quotechar='"')
        list_of_jobs = []
        for row in jobs_data:
            list_of_jobs.append(row)
    return list_of_jobs
