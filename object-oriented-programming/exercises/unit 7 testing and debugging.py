class Task:
    def __init__(self, name: str, done: bool = False):
        self.name = name
        self.done = done

    def mark_done(self):
        self.done = True


class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(task)
        task = Task(name)
        self.tasks.append(task)

    def mark_done(self, index: int):
        self.tasks[index].mark_done()

    def show_tasks(self):
        for task in self.tasks:
            status = "✓" if task.done else "✗"

            print(status, task.name)


task = ["Task 1", "Task 2", "Task 3"]
todolist = ["Buy Milk", "Finish OOP"]
print(task)
print(todolist)

todolist = TodoList()

task1 = Task("Task 1", True)
task2 = Task("Task 2", False)
task3 = Task("Task 3", True)
print(f"{task1.mark_done()}")
print(f"{task2.mark_done()}")
print(f"{task3.mark_done()}")
