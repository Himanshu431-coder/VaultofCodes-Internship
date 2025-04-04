# **To-Do List Application Using Python**  

## **Project Overview**
The **To-Do List Application using Python** is an innovative and user-friendly desktop application developed as part of my final internship project with **VaultOfCodes**. This project leverages the power of **Python** programming along with the **Tkinter** library to create a fully functional to-do list app. The app allows users to manage their tasks effectively by providing an intuitive interface to add, delete, and mark tasks as completed. Additionally, it utilizes various Python modules such as **random** , **pickle** and **Tkinter MessageBox** to enhance functionality and user experience.

---

## **Key Features**
- **Task Management**: Easily add, delete, and update tasks in the to-do list.
- **Filter Tasks on Priority Level**:Users can filter their tasks based on priority (High,Medium,Low).
- **Task Completion**: Users can mark tasks as complete with a single click, and tasks are visually updated to show their status.
- **Random Task Suggestion**: The app can suggest random tasks from the list to encourage users to stay on track.
- **User Notifications**: Error and success messages are provided using Tkinter MessageBox for better user interaction.
- **Simple and Intuitive Interface**: Developed using **Tkinter**, the graphical interface is lightweight, easy to use, and offers a seamless experience.

---

## **Technologies Used**
- **Programming Language**: Python  
- **GUI Library**: Tkinter  
- **Other Modules**:  
    - **Tkinter MessageBox** (for pop-up notifications)
    - **Random** (for random task suggestions)
  
---

## **How to Clone and Run the Project:**

### **Prerequisites**
To ensure a smooth setup and execution of the project, please make sure you have the following installed on your system:
- Python (preferably version 3.7 or higher)
- Tkinter library (usually included with Python)

---

### **Steps to Clone and Run the Project**

1. **Clone the Repository**:  
   Open your terminal or command prompt and execute the following command:
   ```bash
   git clone https://github.com/yourusername/todo-list-python
   ```

2. **Navigate to the Project Directory**:  
   After cloning the repository, change your directory to the project folder:
   ```bash
   cd todo_list
   ```

3. **Install Required Dependencies**:  
   Tkinter is typically bundled with Python, but if it's missing, you can install it via:
   ```bash
   pip install tkinter
   ```

4. **Run the Application**:  
   To run the To-Do List application, execute the following Python script:
   ```bash
   python task.py
   python todo.py
   ```

5. **Use the Application**:  
   The application window will pop up, where you can start adding, deleting, or completing your tasks. Enjoy staying organized!

---

## **File Structure**

```
File Structure
bash
Copy
todo-list-python/
│
├── task.py         # Contains the task-related functionalities (e.g., adding, deleting tasks)
├── todo.py         # Main file where the Tkinter UI is created and the app logic runs
├── tasks.json      # Stores the tasks and their status (persistent data storage)
└── requirements.txt # (Optional) If you need to list any dependencies for the project

task.py: This file manages the core functionality of the to-do list, such as adding tasks, deleting tasks, and managing their status.

todo.py: This is the main script that sets up the graphical user interface (GUI) using Tkinter. It integrates task.py to provide a smooth user experience and includes the logic for interacting with the to-do list.

tasks.json: This file is used for persistent storage of tasks. It stores tasks and their completion status in a JSON format, ensuring that tasks remain saved even after the app is closed and reopened.

---
## **Screenshots**
1. Main Application Window

2. Task Added to the List

3. Task Marked as Complete

4. Random Task Suggestion

Learning Outcomes
Throughout this internship, I gained significant practical experience in:

Designing and building GUI applications using Tkinter.

Implementing core features like task management and notifications in a to-do list application.

Leveraging Python's standard libraries to enhance app functionality, such as using random for task suggestions and MessageBox for error handling and user interaction.

Structuring and organizing code for clean, maintainable projects, making it easy to extend with additional features in the future.

This project not only improved my technical skills but also deepened my understanding of how to create applications that are both practical and engaging for end-users.

Acknowledgements
I would like to express my heartfelt gratitude to VaultOfCodes for providing this opportunity to learn and grow through this hands-on project. Their mentorship helped me achieve both personal and technical growth.

I would also like to thank Tkinter for being a powerful tool in creating simple and effective GUI applications, and to Python for providing the versatility needed for this project.

---

