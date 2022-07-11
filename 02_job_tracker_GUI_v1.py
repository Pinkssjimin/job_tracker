# 13COS Jimin Ahn
# AS 91906
# 08/07/2022

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Job:
    def __init__(self):

        # GUI to get job information

        # Job tracker heading (row 1)
        self.entry_frame = LabelFrame(text="Add New Job",
                                       font="Arial 19 bold")
        self.entry_frame.grid(row=1, padx=10, pady=10)

        # entry frame for inputs
        info_frame = LabelFrame(self.entry_frame)
        info_frame.grid(row=1, columnspan=2, pady=10, padx=10)

        # variables for entry inputs
        self.name_var = StringVar()
        self.dist_var = StringVar()
        self.time_var = StringVar()
        self.wof_var = BooleanVar()

        # name entry (row 2)
        # name entry title
        self.name_entry_label = Label(info_frame, text="Customer Name: ",
                                      font="Arial 14 bold")
        self.name_entry_label.grid(row=1, column=0)

        # Name Entry Box
        self.name_entry = Entry(info_frame, textvariable=self.name_var, font="Arial 14")
        self.name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # job number entry (row 3)

        # distance entry (row 4)
        # distance entry title
        self.dist_entry_label = Label(info_frame, text="Distance Travelled: ",
                                      font="Arial 14 bold")
        self.dist_entry_label.grid(row=2, column=0, padx=10, pady=10)

        # distance Entry Box
        self.dist_entry = Spinbox(info_frame, from_=0, to=1600, textvariable=self.dist_var, width=5)
        self.dist_entry.grid(row=2, column=1)

        # scale label
        self.dist_scale = Label(info_frame, text="km", font="Arial 14", justify=LEFT)
        self.dist_scale.grid(row=2, column=2)

        # Virus protection entry (row 5)
        # virus protection entry title
        self.virus_entry_label = Label(info_frame, text="Virus Protection Time: ",
                                      font="Arial 14 bold")
        self.virus_entry_label.grid(row=3, column=0, pady=10, padx=10)

        # virus protection Entry Box
        self.virus_entry = Spinbox(info_frame, from_=0, to=360, textvariable=self.time_var, width=5)
        self.virus_entry.grid(row=3, column=1, pady=10)

        # scale label (minutes)
        self.virus_scale = Label(info_frame, text="min", font="Arial 14")
        self.virus_scale.grid(row=3, column=2)

        # WOF and tune entry (row 6)
        # wof entry title
        self.wof_entry_label = Label(info_frame, text="WoF & Tune: ",
                                      font="Arial 14 bold")
        self.wof_entry_label.grid(row=4, column=0, padx=10)

        # WoF Entry Box
        self.wof_checkbox = Checkbutton(info_frame, text="yes", variable=self.wof_var)
        self.wof_checkbox.grid(row=4, column=1, columnspan=2)

        # Save button (row 7)
        self.save_btn = Button(text="Save",
                               command=lambda: self.to_display())
        self.save_btn.grid(row=5, pady=10)

    def to_display(self):
        customer_name = self.name_var.get()
        dist = float(self.dist_var.get())
        virus_protection = float(self.time_var.get())
        wof_tune = self.wof_var.get()

        Display(self, customer_name, dist, virus_protection, wof_tune)

class Display:
    def __init__(self, partner, customer_name, distance, virus_protection, wof_tune):
        print(customer_name, distance, virus_protection, wof_tune)

        # partner allows us to disable the button and not spawn multiple boxes
        partner.save_btn.config(state=DISABLED)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Job Tracker")
    something = Job()
    root.mainloop()



