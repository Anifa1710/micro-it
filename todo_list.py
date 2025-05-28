import tkinter as tk
from tkinter import messagebox

# Main application class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_input = tk.Entry(self.root, width=40)
        self.task_input.pack(pady=10)

        self.add_btn = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_btn.pack()

        self.task_listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.done_btn = tk.Button(self.root, text="Mark as Done", width=20, command=self.mark_done)
        self.done_btn.pack()

        self.delete_btn = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_btn.pack()

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append({"title": task, "done": False})
            self.refresh_tasks()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Select a task to mark as done.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.refresh_tasks()
        else:
            messagebox.showinfo("Info", "Select a task to delete.")

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['title']}")

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
