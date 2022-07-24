# 13COS Jimin Ahn
# AS 91906
# 17/07/2022

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self):

        # background colour
        background_colour = "light pink"
        entry_font = "Arial 8"



        # job tracker frame
        self.job_frame = Frame(bg=background_colour, pady=10)
        self.job_frame.grid()

        # title
        logo_label = Label(self.job_frame, text="Suzy's Professional Mobile Service",
                           pady=10, padx=10)
        logo_label.grid(row=0)

        # Job tracker heading (row 1)
        self.entry_frame = LabelFrame(self.job_frame, highlightbackground="black", highlightthickness=1)
        self.entry_frame.grid(row=1, padx=10, pady=10)

        # title for add new job
        self.add_job_label = Label(self.entry_frame, text="Add New Job", fg="grey")
        self.add_job_label.grid(row=0, columnspan=4, padx=20, pady=10)

        # variables for entry inputs
        self.name_var = StringVar()
        self.dist_var = StringVar()
        self.time_var = StringVar()
        self.wof_var = BooleanVar()

        # name entry (row 2)
        # name entry title
        self.name_entry_label = Label(self.entry_frame, text="Customer Name: ",
                                      font=entry_font)
        self.name_entry_label.grid(row=1, column=0, sticky="E", padx=(10,0), pady=(10,0))

        # Name Entry Box
        self.name_entry = Entry(self.entry_frame, textvariable=self.name_var, font=entry_font)
        self.name_entry.grid(row=1,  column=1, columnspan=3, sticky="W", padx=10, pady=(10,0))

        # job number entry (row 3)

        # distance entry  (row 4)
        # distance entry title
        self.dist_entry_label = Label(self.entry_frame, text="Distance Travelled: ",
                                      font=entry_font)
        self.dist_entry_label.grid(row=2, column=0, sticky="E", padx=(10,0), pady=(10,0))

        # distance Entry Box
        self.dist_entry = Spinbox(self.entry_frame, from_=0, to=1600, textvariable=self.dist_var, width=8)
        self.dist_entry.grid(row=2, column=1, sticky="W", padx=(10,0), pady=(10,0))

        # scale label
        self.dist_scale = Label(self.entry_frame, text="km", font=entry_font, justify=LEFT)
        self.dist_scale.grid(row=2, column=2, sticky="W", padx=(0,10), pady=(10,0))

        # Virus protection entry (row 5)
        # virus protection entry title
        self.virus_entry_label = Label(self.entry_frame, text="Virus Protection Time: ",
                                      font=entry_font)
        self.virus_entry_label.grid(row=3, column=0, sticky="E", padx=(10,0), pady=(10,0))

        # virus protection Entry Box
        self.virus_entry = Spinbox(self.entry_frame, from_=0, to=360, textvariable=self.time_var, width=8)
        self.virus_entry.grid(row=3, column=1, sticky="W", padx=(10,0), pady=(10,0))

        # scale label (minutes)
        self.virus_scale = Label(self.entry_frame, text="min", font=entry_font)
        self.virus_scale.grid(row=3, column=2, sticky="W", padx=(0,10), pady=(10,0))

        # WOF and tune entry (row 6)
        # wof entry title
        self.wof_entry_label = Label(self.entry_frame, text="WoF & Tune: ",
                                      font=entry_font)
        self.wof_entry_label.grid(row=4, column=0, sticky="E", padx=(10,0), pady=10)

        # WoF Entry Box
        self.wof_checkbox = Checkbutton(self.entry_frame, text="yes", variable=self.wof_var)
        self.wof_checkbox.grid(row=4, column=1, sticky="W", padx=(10,0), pady=10)

        # Save button (row 7)
        self.save_btn = Button(self.job_frame, text="Save",
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
    root.title("Suzy's Professional Mobile Service")
    something = Start()
    root.mainloop()



