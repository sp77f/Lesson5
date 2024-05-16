class Task:
    def __init__(self, name, description, due_date,  status):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status
    def mark_task(self):
        self.status = status_global[1]  # Change the status    # .
tasks = []
global status_global
status_global = ("Новая", "Выполнено", "В работе")
def add_task():
    name = input("Task name: ")
    description = input("Task description: ")
    due_date = input("Task due date: ")
    status = status_global[0]
    task = Task(name, description, due_date, status)
    tasks.append(task)

def display_undone_tasks():
    print('Не выполненные задачи')
    for task in tasks:
        if task.status != status_global[1]:
            print(task.name, task.description, task.due_date, task.status)

task = Task("Задача 1", "описание 1", "01.01.2024", "Выполнено")
tasks.append(task)
task = Task("Задача 2", "описание 2", "01.03.2024", "Новая")
tasks.append(task)
task = Task("Задача 3", "описание 3", "01.04.2024", "В работе")
tasks.append(task)
print("Все задачи:")
for task in tasks:
    print(task.name, task.description, task.due_date, task.status)
print("Добавляем новую задачу:")
add_task()

task = tasks[1]
task.mark_task()

display_undone_tasks()
print("Все задачи:")
for task in tasks:
    print(task.name, task.description, task.due_date, task.status)