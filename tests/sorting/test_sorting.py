from src.sorting import sort_by


jobs_mock = [
    {"min_salary": 9000, "max_salary": 40000, "date_posted": "2020-04-02"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-06-06"},
    {"min_salary": 1300, "max_salary": 2500, "date_posted": "2020-03-07"},
    {"min_salary": 2500, "max_salary": 4000, "date_posted": "2020-07-10"},
    {"min_salary": 4000, "max_salary": 7000, "date_posted": "2020-01-02"},
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "max_salary")
    assert jobs_mock[0]["max_salary"] == 40000
    assert jobs_mock[-1]["max_salary"] == 2500

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock[0]["min_salary"] == 1300
    assert jobs_mock[-1]["min_salary"] == 9000

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock[0]["date_posted"] == "2020-07-10"
    assert jobs_mock[-1]["date_posted"] == "2020-01-02"
