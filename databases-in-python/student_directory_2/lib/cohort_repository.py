from cohort import Cohorts
from student import Students

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohort_id):
        rows = self._connection.execute('SELECT * FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohorts.id = %s', [cohort_id])
        students = []
        for row in rows:
            student = Students(row["id"], row["student_name"], row["cohort_id"])
            students.append(student)
            print(row)
            cohorts = Cohorts(row[0]["id"], row[0]["cohort_name"], row[0]["starting_date"], students)
        return cohorts


