# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    def __init__(self, task, time_task, status):
        self.task = task
        self.time_task = time_task
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Добавлена задача - {task.task}')

    def mark_task(self, task_description):
        for task in self.tasks:
            if task.task == task_description:
                task.status = 'выполнено'
                print(f'Задача выполнена - {task.task}')

    def print_tasks(self):
        print('Текущие задачи:')
        for task in self.tasks:
            if task.status == 'не выполнено':
                print(f'- {task.task}')

task_manager = TaskManager()

task1 = Task('помыть пол', '1 час', 'не выполнено')
task2 = Task('постирать кота', '1 час', 'не выполнено')
task3 = Task('сделать домашку', '2 дня', 'не выполнено')
task4 = Task('пойти погулять', 'полчаса', 'выполнено')

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)
task_manager.add_task(task4)

task_manager.print_tasks()

task_manager.mark_task('помыть пол')
task_manager.print_tasks()



