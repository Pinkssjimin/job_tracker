# 13COS Jimin Ahn
# AS 91906
# 17/07/2022 - calculating charge

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self):

        # background colour
        background_colour = "light pink"
        entry_font = "Arial 11"

        # job tracker frame
        self.job_frame = Frame(bg=background_colour, pady=10)
        self.job_frame.grid()

        # title
        logo_photo = PhotoImage(file="logo.png")
        self.logo_label = Label(self.job_frame, image=logo_photo)
        self.logo_label.photo = logo_photo
        self.logo_label.grid(row=0)

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
                               command=lambda: self.job_info())
        self.save_btn.grid(row=5, pady=10)

    def job_info(self):
        # covnert distance and time to floats

            dist = float(self.dist_var.get())
            time = float(self.time_var.get())

            # check if all info in correct
            print(self.name_var.get(), dist, time, self.wof_var.get())
            Job(self.name_var.get(), dist, time, self.wof_var.get())

class Job:
    def __init__(self, customer_name, distance, virus_protection, wof_tune):
        #list to store jobs
        self.jobs = []

        self.name = customer_name
        self.dist = distance
        self.time = virus_protection
        self.wof = wof_tune

        self.calc_charge(self.name, self.dist, self.time, self.wof)

    def calc_charge(self, name, dist, time, wof):
        avg_charge = 10
        # additional charge rate for distance over 5km
        dist_rate = 0.5
        # rounding the distance to whole number
        round_dist = round(self.dist)
        # cacluating charge for distance over 5km
        over_dist = round_dist - 5

        # checking if distance is over 5km or not
        # below or equal to 5km
        if over_dist <= 0:
            dist_charge = avg_charge
        # for distnace over 5km
        elif over_dist > 0:
            dist_charge = avg_charge + over_dist * dist_rate

        # charge rate for virus protection minutes
        time_rate = 0.8
        # charge for virus protection time spent
        time_charge = self.time * time_rate

        # charge for wof and tune
        if self.wof == True:
            wof_charge = 100
        else:
            wof_charge = 0

        # total charge for job
        charge = dist_charge + time_charge + wof_charge
        self.jobs.append(charge)
        print(self.jobs)
        #return final charge



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Start()
    root.mainloop()



