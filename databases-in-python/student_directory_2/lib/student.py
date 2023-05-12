class Students:
    def __init__(self, id, student_name, cohort_id):
        self.id = id
        self.student_name = student_name
        self.cohort_id = cohort_id
        


    def __eq__(self, other):
        return self.__dict__ == other.__dict__