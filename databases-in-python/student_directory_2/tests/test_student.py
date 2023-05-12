from lib.student import Students

"""Instantiate variables"""
def test_variables():
    student = Students(1, "Test Name", 1)
    assert student.id == 1
    assert student.student_name == "Test Name"
    assert student.cohort_id == 1
    