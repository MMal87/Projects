from lib.cohort import Cohorts
from lib.student import Students

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohort_id):
        rows = self._connection.execute('SELECT cohorts.id AS id, cohorts.cohort_name, cohorts.starting_date, students.id AS student_id, students.student_name, students.cohort_id FROM cohorts JOIN students ON cohorts.id = students.cohort_id WHERE cohorts.id = %s', [cohort_id])
        students = []
        for row in rows:
            print(f"Position 1 {row}")
            student = Students(row["student_id"], row["student_name"], row["cohort_id"])
            students.append(student)
            
            
        cohort = Cohorts(rows[0]["id"], rows[0]["cohort_name"], rows[0]["starting_date"], students)
        print(f"Position 2 {cohort}")
        return cohort


