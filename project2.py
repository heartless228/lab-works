from rx import Observable, Observer

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

class TodoListObserver(Observer):
    def __init__(self, todolist):
        self.todolist = todolist

    def on_next(self, task):
        self.todolist.add_task(task)
        self.print_tasks()

    def on_error(self, error):
        print("Error:", error)

    def on_completed(self):
        print("Todo list completed")

    def print_tasks(self):
        print("Tasks:", self.todolist.tasks)

# Создаем экземпляр класса TodoList
todo_list = TodoList()

# Создаем экземпляр класса TodoListObserver и передаем ему todo_list
observer = TodoListObserver(todo_list)

# Создаем Observable, который будет эмитировать добавление задачи каждую секунду
task_observable = Observable.interval(1000).map(lambda i: f"Task {i}")

# Подписываемся на Observable и передаем ему нашего observer
task_subscription = task_observable.subscribe(observer)

# Останавливаем Observable через 5 секунд
Observable.timer(5000).subscribe(lambda _: task_subscription.dispose())
