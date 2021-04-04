from todo_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        found = [t for t in self.tasks if t == new_task]
        if found:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        found = [t for t in self.tasks if t.name == task_name]
        if not found:
            return f"Could not find task with the name {task_name}"
        the_task = found[0]
        the_task.completed = True
        return f"Completed task {the_task.name}"

    def clean_section(self):
        not_completed = [t for t in self.tasks if not t.completed]
        amount = len(self.tasks) - len(not_completed)
        self.tasks = not_completed
        return f"Cleared {amount} tasks."

    def view_section(self):
        output = f"Section {self.name}:\n"
        for t in self.tasks:
            output += t.details() + '\n'
        return output


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
