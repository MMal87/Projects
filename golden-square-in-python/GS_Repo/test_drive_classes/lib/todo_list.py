

class TodoList:
    def __init__(self):
        self.todolist = []
    def add(self, todo):
        self.todolist.append(todo)
    def incomplete(self):
        return [todo for todo in self.todolist if not todo.complete]
    def complete(self):
        return [todo for todo in self.todolist if todo.complete]
    def give_up(self):
        for todo in self.todolist:
            todo.mark_complete()


