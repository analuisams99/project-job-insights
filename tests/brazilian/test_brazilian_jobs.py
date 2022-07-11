from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    dict_jobs = read_brazilian_file(path)
    assert ("title" in dict_jobs[0]) is True
    assert ("salary" in dict_jobs[0]) is True
    assert ("type" in dict_jobs[0]) is True
