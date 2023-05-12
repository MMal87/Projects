class Cohorts:
    def __init__(self, id, cohort_name, starting_date, students = None):
        self.id = id
        self.cohort_name = cohort_name
        self.starting_date = starting_date
        self.students = students or []

