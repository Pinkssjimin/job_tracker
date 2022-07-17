# 13COS Jimin Ahn
# AS 91906
# 17/07/2022

from tkinter import *
from functools import partial   # To prevent unwanted windows

class Start:
    def __init__(self):

        # background colour
        background_colour = "light pink"

        # initialise list to hold jobs
        self.job_list = []

        # job tracker frame
        self.job_frame = Frame(bg=background_colour, pady=10)
        self.job_frame.grid()

        # banner image
        self.logo = PhotoImage(file="job_tracker\logo.GIF")
        logo_label = Label(self.job_frame, image=self.logo, pady=10, padx=10)
        logo_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Start()
    root.mainloop()



