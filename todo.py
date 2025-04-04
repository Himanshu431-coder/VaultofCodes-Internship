import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class Task:
    def __init__(self, title, description, category, priority, deadline, sub_tasks):
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.deadline = deadline
        self.sub_tasks = sub_tasks
        self.completed = False

    def is_overdue(self):
        if self.deadline:
            deadline_date = datetime.strptime(self.deadline, '%Y-%m-%d')
            return deadline_date < datetime.now()
        return False

    def mark_completed(self):
        self.completed = True

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = self.load_tasks()
        self.task_number = 0

        # Create main frames
        self.main_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.main_frame.pack(fill='both', expand=True)

        self.header_frame = tk.Frame(self.main_frame, bg='#3498db')
        self.header_frame.pack(fill='x')

        self.content_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.content_frame.pack(fill='both', expand=True)

        self.footer_frame = tk.Frame(self.main_frame, bg='#3498db')
        self.footer_frame.pack(fill='x')

        # Create header widgets
        self.header_label = tk.Label(self.header_frame, text='To-Do List Application', font=('Arial', 18), bg='#3498db', fg='white')
        self.header_label.pack(pady=10)

        # Create content widgets
        self.content_label = tk.Label(self.content_frame, text='Choose an option:', font=('Arial', 14), bg='#f0f0f0')
        self.content_label.pack(pady=10)

        self.option_frame = tk.Frame(self.content_frame, bg='#f0f0f0')
        self.option_frame.pack()

        self.add_task_button = tk.Button(self.option_frame, text='Add Task', command=self.add_task, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.add_task_button.pack(side='left', padx=10)

        self.view_tasks_button = tk.Button(self.option_frame, text='View Tasks', command=self.view_tasks, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.view_tasks_button.pack(side='left', padx=10)

        self.filter_tasks_button = tk.Button(self.option_frame, text='Filter Tasks', command=self.filter_tasks, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.filter_tasks_button.pack(side='left', padx=10)

        self.mark_task_completed_button = tk.Button(self.option_frame, text='Mark Task as Completed', command=self.mark_task_completed, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.mark_task_completed_button.pack(side='left', padx=10)

        self.delete_task_button = tk.Button(self.option_frame, text='Delete Task', command=self.delete_task, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.delete_task_button.pack(side='left', padx=10)

        self.exit_button = tk.Button(self.option_frame, text='Exit', command=self.exit_app, font=('Arial', 12), bg='#e74c3c', fg='white')
        self.exit_button.pack(side='left', padx=10)

        # Create footer widgets
        self.footer_label = tk.Label(self.footer_frame, text='Made by-Himanshu Tapde', font=('Arial', 12), bg='#3498db', fg='white')
        self.footer_label.pack(pady=10)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                return [Task(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f, indent=4)

    def add_task(self):
        self.add_task_window = tk.Toplevel(self.root)
        self.add_task_window.title('Add Task')

        self.title_label = tk.Label(self.add_task_window, text='Title:', font=('Arial', 12))
        self.title_label.pack()

        self.title_entry = tk.Entry(self.add_task_window, font=('Arial', 12))
        self.title_entry.pack()

        self.description_label = tk.Label(self.add_task_window, text='Description:', font=('Arial', 12))
        self.description_label.pack()

        self.description_entry = tk.Entry(self.add_task_window, font=('Arial', 12))
        self.description_entry.pack()

        self.category_label = tk.Label(self.add_task_window, text='Category:', font=('Arial', 12))
        self.category_label.pack()

        self.category_entry = tk.Entry(self.add_task_window, font=('Arial', 12))
        self.category_entry.pack()

        self.priority_label = tk.Label(self.add_task_window, text='Priority:', font=('Arial', 12))
        self.priority_label.pack()

        self.priority_var = tk.StringVar(self.add_task_window)
        self.priority_var.set('Medium')
        self.priority_option = tk.OptionMenu(self.add_task_window, self.priority_var, 'High', 'Medium', 'Low')
        self.priority_option.pack()

        self.deadline_label = tk.Label(self.add_task_window, text='Deadline:', font=('Arial', 12))
        self.deadline_label.pack()

        self.deadline_entry = tk.Entry(self.add_task_window, font=('Arial', 12))
        self.deadline_entry.pack()

        self.sub_tasks_label = tk.Label(self.add_task_window, text='Sub-tasks:', font=('Arial', 12))
        self.sub_tasks_label.pack()

        self.sub_tasks_entry = tk.Entry(self.add_task_window, font=('Arial', 12))
        self.sub_tasks_entry.pack()

        self.add_task_button = tk.Button(self.add_task_window, text='Add Task', command=self.add_task_to_list, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.add_task_button.pack()

    def add_task_to_list(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        priority = self.priority_var.get()
        deadline = self.deadline_entry.get()
        sub_tasks = self.sub_tasks_entry.get().split(',')

        new_task = Task(title, description, category, priority, deadline, sub_tasks)
        self.tasks.append(new_task)

        self.add_task_window.destroy()
        messagebox.showinfo('Task Added', 'Task added successfully!')

    def view_tasks(self):
        self.view_tasks_window = tk.Toplevel(self.root)
        self.view_tasks_window.title('View Tasks')

        self.tasks_text = tk.Text(self.view_tasks_window, font=('Arial', 12))
        self.tasks_text.pack()

        for i, task in enumerate(self.tasks):
            self.tasks_text.insert('end', f'Task {i+1}:\n')
            self.tasks_text.insert('end', f'Title: {task.title}\n')
            self.tasks_text.insert('end', f'Description: {task.description}\n')
            self.tasks_text.insert('end', f'Category: {task.category}\n')
            self.tasks_text.insert('end', f'Priority: {task.priority}\n')
            self.tasks_text.insert('end', f'Deadline: {task.deadline}\n')
            self.tasks_text.insert('end', f'Sub-tasks: {", ".join(task.sub_tasks)}\n\n')

    def filter_tasks(self):
        self.filter_tasks_window = tk.Toplevel(self.root)
        self.filter_tasks_window.title('Filter Tasks')

        self.priority_var = tk.StringVar(self.filter_tasks_window)
        self.priority_var.set('High')
        self.priority_option = tk.OptionMenu(self.filter_tasks_window, self.priority_var, 'High', 'Medium', 'Low')
        self.priority_option.pack()

        self.filter_tasks_button = tk.Button(self.filter_tasks_window, text='Filter Tasks', command=self.filter_tasks_by_priority, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.filter_tasks_button.pack()

    def filter_tasks_by_priority(self):
        priority = self.priority_var.get()
        filtered_tasks = [task for task in self.tasks if task.priority == priority]

        self.filtered_tasks_window = tk.Toplevel(self.root)
        self.filtered_tasks_window.title('Filtered Tasks')

        self.filtered_tasks_text = tk.Text(self.filtered_tasks_window, font=('Arial', 12))
        self.filtered_tasks_text.pack()

        for i, task in enumerate(filtered_tasks):
            self.filtered_tasks_text.insert('end', f'Task {i+1}:\n')
            self.filtered_tasks_text.insert('end', f'Title: {task.title}\n')
            self.filtered_tasks_text.insert('end', f'Description: {task.description}\n')
            self.filtered_tasks_text.insert('end', f'Category: {task.category}\n')
            self.filtered_tasks_text.insert('end', f'Priority: {task.priority}\n')
            self.filtered_tasks_text.insert('end', f'Deadline: {task.deadline}\n')
            self.filtered_tasks_text.insert('end', f'Sub-tasks: {", ".join(task.sub_tasks)}\n\n')

    def mark_task_completed(self):
        self.mark_task_completed_window = tk.Toplevel(self.root)
        self.mark_task_completed_window.title('Mark Task as Completed')

        self.task_number_label = tk.Label(self.mark_task_completed_window, text='Enter task number:', font=('Arial', 12))
        self.task_number_label.pack()

        self.task_number_entry = tk.Entry(self.mark_task_completed_window, font=('Arial', 12))
        self.task_number_entry.pack()

        self.mark_task_completed_button = tk.Button(self.mark_task_completed_window, text='Mark Task as Completed', command=self.mark_task_as_completed, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.mark_task_completed_button.pack()

    def mark_task_as_completed(self):
        task_number = int(self.task_number_entry.get()) - 1
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            messagebox.showinfo('Task Marked as Completed', 'Task marked as completed!')
        else:
            messagebox.showerror('Invalid Task Number', 'Invalid task number.')

    def delete_task(self):
        self.delete_task_window = tk.Toplevel(self.root)
        self.delete_task_window.title('Delete Task')

        self.task_number_label = tk.Label(self.delete_task_window, text='Enter task number:', font=('Arial', 12))
        self.task_number_label.pack()

        self.task_number_entry = tk.Entry(self.delete_task_window, font=('Arial', 12))
        self.task_number_entry.pack()

        self.delete_task_button = tk.Button(self.delete_task_window, text='Delete Task', command=self.delete_task_from_list, font=('Arial', 12), bg='#e74c3c', fg='white')
        self.delete_task_button.pack()

    def delete_task_from_list(self):
        task_number = int(self.task_number_entry.get()) - 1
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
            messagebox.showinfo('Task Deleted', 'Task deleted successfully!')
        else:
            messagebox.showerror('Invalid Task Number', 'Invalid task number.')

    def exit_app(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('To-Do List Application')
    app = ToDoListApp(root)
    root.mainloop()
