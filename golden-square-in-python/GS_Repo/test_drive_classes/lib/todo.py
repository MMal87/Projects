class Todo:
    def __init__(self, task):

        self.task = task
        self.complete = False
    def mark_complete(self):
        if self.task == "":
            raise Exception("Please enter a task:")
        self.complete = True


        