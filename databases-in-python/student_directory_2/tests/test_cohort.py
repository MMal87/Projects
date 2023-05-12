from lib.cohort import Cohorts

"""Instantiate variables"""
def test_variables():
    cohort = Cohorts(1, "Test Name", '2022-01-01')
    assert cohort.id == 1
    assert cohort.cohort_name == "Test Name"
    assert cohort.starting_date == '2022-01-01'
    