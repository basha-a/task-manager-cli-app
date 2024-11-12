# task_manager.py

import json

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data["id"], data["title"], data["completed"])

#-------------------

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        print(f"Task '{title}' added with ID {task_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

    def delete_task(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task with ID {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_task_as_complete(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.completed = True
            print(f"Task with ID {task_id} marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

#----------------------

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved to tasks.json.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
                print("Tasks loaded from tasks.json.")
        except FileNotFoundError:
            print("No existing tasks file found. Starting fresh.")

#---------------------

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            task_manager.add_task(title)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_task_as_complete(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "5":
            task_manager.save_tasks()
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
