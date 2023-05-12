from lib.cohort_repository import CohortRepository
from lib.cohort import Cohorts
from lib.student import Students


"""When we call #find_all it will return the requested items"""

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    result = repository.find_with_students(1)

    assert result == Cohorts(1, 'Cohort 1', '2022-01-01', [Students(1, 'John Smith', 1), Students(2, 'Jane Doe', 1)])