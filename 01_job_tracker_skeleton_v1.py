# 13COS Jimin Ahn
# AS 91906
# 07/07/2022

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Job:
    def __init__(self):

        # GUI to get job information
        self.job_frame = Frame(pady=10, padx=10)
        self.job_frame.grid()

        # Job tracker heading (row 0)
        self.job_tracker_label = Label(self.job_frame, text="Add New Job",
                                       font="Arial 19 bold")
        self.job_tracker_label.grid(row=0)

        self.name_entry_frame = Frame(self.job_frame)
        self.name_entry_frame.grid(row=1, pady=10)
        # name entry title
        self.name_entry_label = Label(self.name_entry_frame, text="Customer Name: ",
                                      font="Arial 14 bold")
        self.name_entry_label.grid(row=0, column=0)

        # Name Entry Box (row 1)
        self.name_entry = Entry(self.name_entry_frame, font="Arial 14")
        self.name_entry.grid(row=0, column=1)

        # Save button (row 2)
        self.save_button = Button(text="Save",
                                  command=lambda: self.to_display())
        self.save_button.grid(row=2, pady=10)

    def to_display(self):
        customer_name = self.name_entry.get()
        Display(self, customer_name)

class Display:
    def __init__(self, partner, name):
        print(name)

        # partner allows us to disable the button and not spawn multiple boxes
        partner.save_button.config(state=DISABLED)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Tracker")
    something = Job()
    root.mainloop()

