import datetime


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_at = datetime.datetime.now()
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}\nCreated at: {self.created_at}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(task)
                print()

    def complete_task(self, task_num):
        if not 1 <= task_num <= len(self.tasks):
            print("Invalid task number.")
        else:
            task = self.tasks[task_num - 1]
            task.mark_as_completed()
            print("Task marked as completed.")


def main():
    todo_list = TodoList()

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_num = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_num)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == '__main__':
    main()