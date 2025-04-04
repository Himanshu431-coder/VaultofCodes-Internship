# task.py
from datetime import datetime

class Task:
    def __init__(self, title, description, category, priority='Medium', deadline=None, sub_tasks=None):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority  # High, Medium, Low
        self.deadline = deadline  # Format: YYYY-MM-DD
        self.completed = False
        self.sub_tasks = sub_tasks if sub_tasks else []  # List of sub-tasks

    def mark_completed(self):
        self.completed = True

    def is_overdue(self):
        if self.deadline:
            return datetime.now() > datetime.strptime(self.deadline, '%Y-%m-%d') and not self.completed
        return False

    def __str__(self):
        status = "✔" if self.completed else "✘"
        deadline = f" | Deadline: {self.deadline}" if self.deadline else ""
        sub_tasks = f" | Sub-Tasks: {', '.join(self.sub_tasks)}" if self.sub_tasks else ""
        return f"Title: {self.title}\nDescription: {self.description}\nCategory: {self.category}\nPriority: {self.priority}\nStatus: {status}{deadline}{sub_tasks}"
