import tkinter as tk
from tkinter import ttk
from reportlab.pdfgen import canvas
from datetime import datetime
import random

# Hardcoded student names
students = ["Student{}".format(i) for i in range(1, 91)]

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")

        # Variables for dropdowns
        self.subject_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.section_var = tk.StringVar()

        # Initialize GUI
        self.create_gui()

    def create_gui(self):
        # Label and Entry for Date
        date_label = tk.Label(self.root, text="Date:")
        date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Dropdown for Subject
        subject_label = tk.Label(self.root, text="Subject:")
        subject_label.grid(row=1, column=0, padx=5, pady=5)
        subjects = ["Math", "Science", "English", "History"]
        subject_dropdown = ttk.Combobox(self.root, textvariable=self.subject_var, values=subjects)
        subject_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Dropdown for Course
        course_label = tk.Label(self.root, text="Course:")
        course_label.grid(row=2, column=0, padx=5, pady=5)
        courses = ["Computer Science", "Biology", "Physics", "History"]
        course_dropdown = ttk.Combobox(self.root, textvariable=self.course_var, values=courses)
        course_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Dropdown for Section
        section_label = tk.Label(self.root, text="Section:")
        section_label.grid(row=3, column=0, padx=5, pady=5)
        sections = ["A", "B", "C", "D"]
        section_dropdown = ttk.Combobox(self.root, textvariable=self.section_var, values=sections)
        section_dropdown.grid(row=3, column=1, padx=5, pady=5)

        # Attendance Tabs (A and P)
        tabs = ttk.Notebook(self.root)
        tabs.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Tab for 'Present' (P)
        present_tab = ttk.Frame(tabs)
        tabs.add(present_tab, text='P')

        # Tab for 'Absent' (A)
        absent_tab = ttk.Frame(tabs)
        tabs.add(absent_tab, text='A')

        # Buttons
        submit_button = tk.Button(self.root, text="Submit", command=self.generate_pdf)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_pdf(self):
        # Get selected values
        date = self.date_entry.get()
        subject = self.subject_var.get()
        course = self.course_var.get()
        section = self.section_var.get()

        # Create PDF
        pdf_filename = "attendance_{}_{}_{}.pdf".format(date, subject, section)
        pdf = canvas.Canvas(pdf_filename)
        pdf.setTitle(pdf_filename)

        # PDF Content
        pdf.drawString(100, 800, "Date: {}".format(date))
        pdf.drawString(100, 780, "Subject: {}".format(subject))
        pdf.drawString(100, 760, "Course: {}".format(course))
        pdf.drawString(100, 740, "Section: {}".format(section))

        # Randomly mark students as present or absent
        for i, student in enumerate(students, start=1):
            status = "P" if random.choice([True, False]) else "A"
            pdf.drawString(100, 720 - i * 20, "{}. {}: {}".format(i, student, status))

        # Save and close PDF
        pdf.save()

        # Display success message
        success_message = "Attendance saved as {}".format(pdf_filename)
        tk.messagebox.showinfo("Success", success_message)

# Main function
def main():
    root = tk.Tk()
    app = AttendanceSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
