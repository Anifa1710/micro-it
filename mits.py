import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MITS UI/UX Design Project")
        self.geometry("800x600")
        self.configure(bg="#f0f4f8")

        self.username = ""
        self.enrolled_courses = []

        self.pages = {}
        self.create_navigation()
        self.create_pages()
        self.show_page("HomePage")

    def create_navigation(self):
        nav_frame = tk.Frame(self, bg="#003366", height=50)
        nav_frame.pack(fill="x")

        buttons = [
            ("Home", "HomePage"),
            ("Login", "LoginPage"),
            ("Dashboard", "DashboardPage"),
            ("Courses", "CoursePage"),
            ("Profile", "ProfilePage"),
            ("About", "AboutPage"),
            ("Contact", "ContactPage"),
        ]

        for text, page in buttons:
            tk.Button(nav_frame, text=text, command=lambda p=page: self.show_page(p),
                      font=("Segoe UI", 10), bg="#0059b3", fg="white", padx=10, pady=5,
                      activebackground="#007acc", bd=0).pack(side="left", padx=2, pady=5)

    def create_pages(self):
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        for PageClass in (HomePage, LoginPage, DashboardPage,
                          CoursePage, ProfilePage, AboutPage, ContactPage):
            page_name = PageClass.__name__
            frame = PageClass(container, self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page_name):
        page = self.pages[page_name]
        if page_name == "DashboardPage":
            page.update_dashboard(self.username, self.enrolled_courses)
        elif page_name == "ProfilePage":
            page.update_profile(self.username)
        elif page_name == "CoursePage":
            course_names = ["Python", "Data Science", "Machine Learning", "Web Development"]
            page.update_course_list(course_names)
        page.tkraise()

    def login_user(self, username):
        self.username = username
        messagebox.showinfo("Success", f"Welcome {username}!")
        self.show_page("DashboardPage")

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            messagebox.showinfo("Enrolled", f"Successfully enrolled in {course}")
            self.pages["DashboardPage"].update_dashboard(self.username, self.enrolled_courses)


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")
        tk.Label(self, text="Welcome to MITS Website", font=("Segoe UI", 20, "bold"),
                 bg="#f0f4f8", fg="#003366").pack(pady=30)
        tk.Label(self, text="This is a UI/UX Prototype built with Tkinter",
                 font=("Segoe UI", 12), bg="#f0f4f8").pack(pady=5)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")
        self.controller = controller

        frame = tk.Frame(self, bg="white", padx=20, pady=20, relief="groove", bd=2)
        frame.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(frame, text="Login", font=("Segoe UI", 16, "bold"), bg="white").grid(row=0, columnspan=2, pady=10)
        tk.Label(frame, text="Username:", font=("Segoe UI", 12), bg="white").grid(row=1, column=0, pady=5, sticky="e")
        self.username_entry = tk.Entry(frame, font=("Segoe UI", 12), width=25)
        self.username_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Password:", font=("Segoe UI", 12), bg="white").grid(row=2, column=0, pady=5, sticky="e")
        self.password_entry = tk.Entry(frame, font=("Segoe UI", 12), width=25, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        tk.Button(frame, text="Login", command=self.login_user, bg="#0059b3", fg="white",
                  font=("Segoe UI", 11), padx=10, pady=5, bd=0, activebackground="#007acc")\
            .grid(row=3, columnspan=2, pady=15)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.controller.login_user(username)
        else:
            messagebox.showerror("Error", "Please enter both username and password.")


class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")
        self.controller = controller

        self.label = tk.Label(self, text="", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#003366")
        self.label.pack(pady=30)

        self.course_listbox = tk.Listbox(self, font=("Segoe UI", 12), width=50, height=10)
        self.course_listbox.pack(pady=10)

    def update_dashboard(self, username, courses):
        self.label.config(text=f"Welcome, {username}!")
        self.course_listbox.delete(0, tk.END)
        for course in courses:
            self.course_listbox.insert(tk.END, course)


class CoursePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")
        self.controller = controller

        tk.Label(self, text="Available Courses", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#003366").pack(pady=20)

        self.search_var = tk.StringVar()
        tk.Entry(self, textvariable=self.search_var, font=("Segoe UI", 12), width=40).pack(pady=5)
        tk.Button(self, text="Search", command=self.filter_courses, font=("Segoe UI", 10),
                  bg="#007acc", fg="white", padx=10, bd=0).pack(pady=5)

        self.course_frame = tk.Frame(self, bg="#f0f4f8")
        self.course_frame.pack(pady=10)

    def update_course_list(self, courses):
        self.full_course_list = courses
        self.display_courses(courses)

    def filter_courses(self):
        keyword = self.search_var.get().lower()
        filtered = [c for c in self.full_course_list if keyword in c.lower()]
        self.display_courses(filtered)

    def display_courses(self, courses):
        for widget in self.course_frame.winfo_children():
            widget.destroy()

        for course in courses:
            frame = tk.Frame(self.course_frame, bg="white", bd=1, relief="solid", padx=10, pady=5)
            frame.pack(fill="x", padx=20, pady=5)

            tk.Label(frame, text=course, font=("Segoe UI", 12), bg="white").pack(side="left")
            tk.Button(frame, text="Enroll", command=lambda c=course: self.controller.enroll_course(c),
                      font=("Segoe UI", 10), bg="#28a745", fg="white", bd=0, padx=10).pack(side="right")


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")
        self.controller = controller

        self.label = tk.Label(self, text="", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#003366")
        self.label.pack(pady=30)

    def update_profile(self, username):
        self.label.config(text=f"User Profile\n\n👤 Username: {username}")


class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")

        tk.Label(self, text="About MITS", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#003366").pack(pady=30)
        tk.Label(self, text="MITS is a prestigious institution offering various engineering and technology programs.",
                 font=("Segoe UI", 12), wraplength=600, justify="center", bg="#f0f4f8").pack(pady=10)


class ContactPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f0f4f8")

        tk.Label(self, text="Contact Us", font=("Segoe UI", 18, "bold"), bg="#f0f4f8", fg="#003366").pack(pady=30)
        tk.Label(self, text="📧 Email: contact@mits.edu\n📞 Phone: +91 12345 67890\n🏫 Address: MITS Campus, India",
                 font=("Segoe UI", 12), bg="#f0f4f8", justify="center").pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
