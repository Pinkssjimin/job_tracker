# 13COS Jimin Ahn
# AS 91906
# 08/07/2022

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Job:
    def __init__(self):

        # GUI to get job information
        self.job_frame = Frame(pady=10, padx=10, highlightbackground="black",
                               highlightthickness=1)
        self.job_frame.grid()

        # Job tracker heading (row 1)
        self.job_tracker_label = Label(self.job_frame, text="Add New Job",
                                       font="Arial 19 bold")
        self.job_tracker_label.grid(row=1)

        # name entry (row 2)
        self.name_entry_frame = Frame(self.job_frame)
        self.name_entry_frame.grid(row=2, pady=10)
        # name entry title
        self.name_entry_label = Label(self.name_entry_frame, text="Customer Name: ",
                                      font="Arial 14 bold", justify=LEFT)
        self.name_entry_label.grid(row=0, column=0)

        # Name Entry Box
        self.name_entry = Entry(self.name_entry_frame, font="Arial 14")
        self.name_entry.grid(row=0, column=1)

        # job number entry (row 3)
        self.job_num_entry_frame = Frame(self.job_frame)
        self.job_num_entry_frame.grid(row=3, pady=10)
        # job number entry title
        self.job_num_entry_label = Label(self.job_num_entry_frame, text="Job Number: ",
                                      font="Arial 14 bold", justify=LEFT)
        self.job_num_entry_label.grid(row=0, column=0)

        # job number Entry Box
        self.job_num_entry = Entry(self.job_num_entry_frame, font="Arial 14",
                                   justify=RIGHT)
        self.job_num_entry.grid(row=0, column=1)

        # distance entry (row 4)
        self.dist_entry_frame = Frame(self.job_frame)
        self.dist_entry_frame.grid(row=4, pady=10)
        # distance entry title
        self.dist_entry_label = Label(self.dist_entry_frame, text="Distance Travelled: ",
                                      font="Arial 14 bold", justify=LEFT)
        self.dist_entry_label.grid(row=0, column=0)

        # distance Entry Box
        self.dist_entry = Entry(self.dist_entry_frame, font="Arial 14", width=5)
        self.dist_entry.grid(row=0, column=1)

        # scale label
        self.dist_scale = Label(self.dist_entry_frame, text="km", font="Arial 14")
        self.dist_scale.grid(row=0, column=2)

        # Virus protection entry (row 5)
        self.virus_entry_frame = Frame(self.job_frame)
        self.virus_entry_frame.grid(row=5, pady=10)
        # virus protection entry title
        self.virus_entry_label = Label(self.virus_entry_frame, text="Virus Protection Time: ",
                                      font="Arial 14 bold", justify=LEFT)
        self.virus_entry_label.grid(row=0, column=0)

        # virus protection Entry Box
        self.virus_entry = Entry(self.virus_entry_frame, font="Arial 14", width=5)
        self.virus_entry.grid(row=0, column=1)

        # scale label (minutes)
        self.virus_scale = Label(self.virus_entry_frame, text="min", font="Arial 14")
        self.virus_scale.grid(row=0, column=2)

        # WOF and tune entry (row 6)
        self.wof_entry_frame = Frame(self.job_frame)
        self.wof_entry_frame.grid(row=6, pady=10)
        # wof entry title
        self.wof_entry_label = Label(self.wof_entry_frame, text="WoF & Tune: ",
                                      font="Arial 14 bold", justify=LEFT)
        self.wof_entry_label.grid(row=0, column=0)

        # WoF Entry Box
        self.wof_checkbox = Checkbutton(self.wof_entry_frame, variable=i,
                                        onvalue=1, offvalue=0)
        self.wof_checkbox.grid(row=0, column=1)

        # Save button (row 7)
        self.save_button = Button(text="Save",
                                  command=lambda: self.to_display())
        self.save_button.grid(row=7, pady=10)

    def to_display(self):
        customer_name = self.name_entry.get()
        job_num = self.job_num_entry.get()
        distance = self.dist_entry.get()
        virus_protection = self.virus_entry.get()
        if i.get() == 1:
            

        Display(self, customer_name, job_num, distance, virus_protection, wof_tune)

class Display:
    def __init__(self, partner, customer_name, job_num, distance, virus_protection, wof_tune):
        print(customer_name, job_num, distance, virus_protection, wof_tune)

        # partner allows us to disable the button and not spawn multiple boxes
        partner.save_button.config(state=DISABLED)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Tracker")
    something = Job()
    root.mainloop()



