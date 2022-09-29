# 13COS Jimin Ahn
# AS 91906
# 29/07/2022 - final

from tkinter import *
from functools import partial   # To prevent unwanted windows
import re

class Job_tracker:
    def __init__(self):
        """
        collecting information of customers
         :return: name, time for service, distanced travelled, WoF
        """

        self.charges = []
        self.names = []

        background_colour = "light pink"
        entry_font = "Arial 12"
        title_font = "Arial 16 bold"
        small_font = "Arial 11"

        # job tracker frame
        self.job_frame = Frame(bg=background_colour, pady=10)
        self.job_frame.grid()

        # title
        logo_photo = PhotoImage(file="logo.png")
        self.logo_label = Label(self.job_frame, image=logo_photo, bg=background_colour)
        self.logo_label.photo = logo_photo
        # self.logo_label = Label(self.job_frame, text="temporary title")
        self.logo_label.grid(row=0, pady=10, padx=0)

        # title for add new job
        self.add_job_label = Label(self.job_frame, text="Add New Job", fg="black", font=title_font, bg=background_colour)
        self.add_job_label.grid(row=1, columnspan=4, padx=20, pady=(10,0))

        # input info text (label ,row 2)
        self.input_text = Label(self.job_frame,
                                text="Enter the job information in the "
                                     "boxes below and press the Save "
                                     "button to save your job.",
                                width=50, bg=background_colour, font=small_font,
                                wrap=250)
        self.input_text.grid(row=2, pady=(0,10))

        # Job tracker heading (row 1)
        self.entry_frame = LabelFrame(self.job_frame, highlightbackground="black", highlightthickness=1)
        self.entry_frame.grid(row=3, padx=10, pady=10)

        # variables for entry inputs
        self.name_var = StringVar()
        self.dist_var = StringVar()
        self.time_var = StringVar()
        self.wof_var = BooleanVar()

        # name entry (row 2)
        # name entry title
        self.name_entry_label = Label(self.entry_frame, text="Customer Name: ",
                                      font=entry_font)
        self.name_entry_label.grid(row=1, column=0, sticky="E", padx=(10,0), pady=(30,0))

        # Name Entry Box
        self.name_entry = Entry(self.entry_frame, textvariable=self.name_var, font=entry_font)
        self.name_entry.grid(row=1,  column=1, columnspan=3, sticky="W", padx=10, pady=(30,0))

        # job number entry (row 3)

        # distance entry  (row 4)
        # distance entry title
        self.dist_entry_label = Label(self.entry_frame, text="Distance Travelled: ",
                                      font=entry_font)
        self.dist_entry_label.grid(row=2, column=0, sticky="E", padx=(10,0), pady=(10,0))

        # distance Entry Box
        self.dist_entry = Spinbox(self.entry_frame, from_=0, to=1600, textvariable=self.dist_var, width=8, font=entry_font)
        self.dist_entry.grid(row=2, column=1, sticky="W", padx=(10,0), pady=(10,0))

        # scale label
        self.dist_scale = Label(self.entry_frame, text="km", font=entry_font, justify=LEFT)
        self.dist_scale.grid(row=2, column=2, sticky="W", padx=(0,10), pady=(10,0))

        self.service_label = Label(self.entry_frame, text="SERVICES", font=small_font, fg="grey")
        self.service_label.grid(row=3, columnspan=4, pady=(10,0), padx=10)
        # Virus protection entry (row 5)
        # virus protection entry title
        self.virus_entry_label = Label(self.entry_frame, text="Virus Protection Time: ",
                                      font=entry_font)
        self.virus_entry_label.grid(row=4, column=0, sticky="E", padx=(10,0), pady=(10,0))

        # virus protection Entry Box
        self.virus_entry = Spinbox(self.entry_frame, from_=0, to=360, textvariable=self.time_var, width=8, font=entry_font)
        self.virus_entry.grid(row=4, column=1, sticky="W", padx=(10,0), pady=(10,0))

        # scale label (minutes)
        self.virus_scale = Label(self.entry_frame, text="min", font=entry_font)
        self.virus_scale.grid(row=4, column=2, sticky="W", padx=(0,10), pady=(10,0))

        # WOF and tune entry (row 6)
        # wof entry title
        self.wof_entry_label = Label(self.entry_frame, text="WoF & Tune: ",
                                      font=entry_font)
        self.wof_entry_label.grid(row=5, column=0, sticky="E", padx=(10,0), pady=10)

        # WoF Entry Box
        self.wof_checkbox = Checkbutton(self.entry_frame, text="yes", variable=self.wof_var, font=entry_font)
        self.wof_checkbox.grid(row=5, column=1, sticky="W", padx=(10,0), pady=10)

        #Label to notify people with errors and success
        self.msg_label = Label(self.entry_frame, wraplength=280, justify=LEFT, font=small_font)
        self.msg_label.grid(row=6, columnspan=3, padx=10, pady=(0, 5))

        #cancel and save button frame(row 6)
        self.save_btn_frame = Frame(self.job_frame, bg=background_colour)
        self.save_btn_frame.grid(row=4, pady=10)

        # Save button (row 6-0)
        self.save_btn = Button(self.save_btn_frame, text="Save",
                               command=lambda: self.job_info())
        self.save_btn.grid(row=0, column=1, padx=0, pady=0)

        # View all jobs entered
        self.show_jobs_btn = Button(self.save_btn_frame, text="Show all jobs",
                                    command=lambda: self.display(self.charges, self.names))
        self.show_jobs_btn.grid(row=0, column=0, padx=10, pady=0)

    def display(self, charges, names):
        """
        Displays all the information entered in a gallery format.

        :param charges: list with the total charges for each customer
        :param names: list with all the names for customer
        :return: job information
        """

        # clear notice board
        self.msg_label.configure(text="")

        Display(self, charges, names)

    def job_info(self):
        """
        error handling for the data entered at Job_tracker class(customer information entering section)

        :return: any error messages for unexpected inputs
        """
        try:
            # clear notice board
            self.msg_label.configure(text="")

            # covnert distance and time to floats
            dist = float(self.dist_var.get())
            time = float(self.time_var.get())

            # check if all info in correct
            if self.name_var.get().strip() != "" and dist >0 and (time > 0 or self.wof_var.get()):
                # print(self.name_var.get(), dist, time, self.wof_var.get())

                self.name = self.name_var.get()
                self.wof = self.wof_var.get()

                self.calc_charge(dist, time)


                # clear all entries once pressed save
                self.msg_label.configure(fg="green", text="Successfully saved")
                self.name_var.set("")
                for var in [self.dist_var, self.time_var, self.wof_var]:
                    var.set(0)

            else:
                error = ""
                if self.name_var.get().strip() == "":
                    error += "Please enter: Customer Name\n"
                if dist <= 0:
                    error += "Please enter: Travelled distance higher than 0\n"
                if time <= 0 and self.wof_var.get() == False:
                    error += "Please enter: At least one service\n- (virus protection higher than 0 or tick WOF & Tune)"

                #error message in red
                self.msg_label.configure(fg="red", text=error)

        except ValueError:
            self.msg_label.configure(fg="red", text="Please enter: Numbers for km travelled and minutes spent")


    def calc_charge(self, dist, time):
        """
        Calculates the total charge for a customer using the data inputted

        :param dist: integer of the distance travelled
        :param time: integer of time taken for service
        :return: Total charge for a job
        """

        avg_charge = 10
        # additional charge rate for distance over 5km
        dist_rate = 0.5
        # rounding the distance to whole number
        round_dist = round(dist)
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
        time_charge = time * time_rate

        # charge for wof and tune
        if self.wof == True:
            wof_charge = 100
        else:
            wof_charge = 0

        # total charge for job
        charge = dist_charge + time_charge + wof_charge
        #return final charge
        self.charges.append(charge)
        self.names.append(self.name)
        # print(self.charges, self.names)

    def close_jobs(self, partner):
        """
        closes the job information entering frame

        :return: destroy the job_frame
        """
     #Put add new job button back to normal
     partner.add_job_btn.config(state=NORMAL)
     self.job_frame.destroy()

class Display:
    def __init__(self, partner, charges, names):

        info_font = "arial 12 italic"

        # background colour
        background_colour = "light pink"

        # disable save & show all jobs button
        partner.save_btn.config(state=DISABLED)
        partner.show_jobs_btn.config(state=DISABLED)

        self.charges = charges
        self.names = names

        # set up child window
        self.display_box = Toplevel()

        # if user press cross at top, closes display and releases show jobs and save button
        self.display_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_display, partner))
        # set up GUI frame
        self.show_jobs_frame = Frame(self.display_box, bg=background_colour)
        self.show_jobs_frame.grid()

        # set up heading
        logo_photo = PhotoImage(file="logo.png")
        self.logo_label = Label(self.show_jobs_frame, image=logo_photo, bg=background_colour)
        self.logo_label.photo = logo_photo
        # self.logo_label = Label(self.show_jobs_frame, text="temporary title")
        self.logo_label.grid(row=0, pady=10, padx=10)

                # export / add job buttons frame (row2)
        self.export_add_job_frame = Frame(self.show_jobs_frame, bg=background_colour)
        self.export_add_job_frame.grid(row=3, pady=10)

        # add job button
        self.add_job_btn = Button(self.export_add_job_frame, text="Add new job",
                                  width=10, command=partial(self.close_display, partner))
        self.add_job_btn.grid(row=0, column=0, padx=10)

        # export button
        self.export_btn = Button(self.export_add_job_frame, text="Export",
                                 width=10, command=lambda: self.to_export(charges, names))
        self.export_btn.grid(row=0, column=1)

        self.current_job = 0

        self.next_prev_frame = Frame(self.show_jobs_frame, bg=background_colour)
        self.next_prev_frame.grid(row=2)

        #previous button

        # number tracker
        self.num_tracker = Label(self.next_prev_frame, bg=background_colour)
        self.num_tracker.grid(row=1, column=1)

        self.prev_btn = Button(self.next_prev_frame, text="<Previous",
                               command=lambda: self.prev_job())
        self.prev_btn.grid(row=1, column=0, pady=10, padx=10)

        #next button
        self.next_btn = Button(self.next_prev_frame, text="Next>",
                               command=lambda: self.next_job())
        self.next_btn.grid(row=1, column=2, pady=10, padx=10)

        job_info = self.show_job()

        # display frame
        self.display_frame = Frame(self.show_jobs_frame, highlightbackground="black", highlightthickness=1)
        self.display_frame.grid(row=1, pady=10, padx=10)

        # job info label
        self.job_info_label = Label(self.display_frame, text=job_info,
                                       font=info_font, justify=LEFT, width=35, wrap=350)
        self.job_info_label.grid(row=0, pady=20, padx=10)

    def next_job(self):
        """clicking on the next arrow button

        :return: adds 1 to the current_job variable which indicates the job number being displayed
        """
        self.current_job += 1
        self.job_info_label.configure(text=self.show_job())

    def  prev_job(self):
        """
        clicking on the prev arrow button

        :return: subtracts 1 to the current_job variable which indicates the job number being displayed
        """
        self.current_job -= 1
        self.job_info_label.configure(text=self.show_job())

    def show_job(self):
        """
        :return: Displays the job summary of the job number according to current_job
        """
        if len(self.charges) == 0:
            job_info = "No jobs entered"
            self.num_tracker.configure(text="0/0")
            # disable next and prev button
            self.next_btn.configure(state=DISABLED)
            self.prev_btn.configure(state=DISABLED)
            self.export_btn.configure(state=DISABLED)

        else:
            # disable next button if last job in list
            if self.current_job == len(self.charges) - 1:
                self.next_btn.configure(state=DISABLED)
            else:
                self.next_btn.configure(state=NORMAL)

            # disable prev button if first job in list
            if self.current_job == 0:
                self.prev_btn.configure(state=DISABLED)
            else:
                self.prev_btn.configure(state=NORMAL)

            job_num = self.current_job + 1
            name = self.names[self.current_job]
            charge = self.charges[self.current_job]
            job_info = "Job number: {}\n" \
                       "Customer name: {}\n" \
                       "Charge: ${:.2f}".format(job_num, name, charge)
            self.num_tracker.configure(text="{}/{}".format(job_num, len(self.charges)))

        return job_info

    def close_display(self, partner):
        """
        When adding new job frame is opened, display frame closes
        :return: save and show all jobs button in the add job frame is set to normal and display frame is destroyed
        """
        # put Show all jobs button and save button normal
        partner.save_btn.config(state=NORMAL)
        partner.show_jobs_btn.config(state=NORMAL)
        self.display_box.destroy()

    def to_export(self, charges, names):
        """
        exports the job summary of all the jobs entered in the list.
        :param charges: list of total charges for each customer
        :param names: list of names of the customers
        :return: data saved in .txt file
        """
        Export(self, charges, names)

class Export:
    def __init__(self, partner, charges, names):

        background = "light blue"

        entry_font = "Arial 12"
        title_font = "Arial 16 bold"
        small_font = "Arial 9"

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # set up child window
        self.export_box = Toplevel()

        # if users press cross at top, closese export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up heading
        logo_photo = PhotoImage(file="logo.png")
        self.logo_label = Label(self.export_frame, image=logo_photo, bg=background)
        self.logo_label.photo = logo_photo
        # self.logo_label = Label(self.show_jobs_frame, text="temporary title")
        self.logo_label.grid(row=0, pady=10, padx=10)


        # set up export heading (row 0)
        self.export_heading = Label(self.export_frame, text="Export",
                                    font=title_font, bg=background)
        self.export_heading.grid(row=1)

        # export text (label ,row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the "
                                      "box below and press the Save "
                                      "button to save your jobs to "
                                      "text file.",
                                 justify=LEFT, width=40, bg=background, font=small_font,
                                 wrap=250)
        self.export_text.grid(row=2)

        # warning text (row 3)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you "
                                      "enter below already "
                                      "exists, its contents "
                                      "will be replaced with your "
                                      "jobs", justify=LEFT, bg="light pink",
                                 fg="maroon", font=small_font, wrap=225,
                                 padx=10, pady=10)
        self.export_text.grid(row=3)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font=entry_font, justify=CENTER)
        self.filename_entry.grid(row=4, pady=10)

        # error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background, font=small_font)
        self.save_error_label.grid(row=5)

        # save / cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame, bg=background)
        self.save_cancel_frame.grid(row=6, pady=10)

        # save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_jobs(partner, charges, names)))
        self.save_button.grid(row=0, column=1, padx=10)

        self.cancel_button = Button(self.save_cancel_frame, text="Back",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=0)

    def save_jobs(self, partner, charges, names):
        """
        error handling name of the exporting file and saving it in .txt file format

        :param charges: list of charges for all the customers
        :param names: list of names of the customers
        :return: available exporting file name or error message when not available.
        """

        # Regular expression to check filename is valid
        has_error = "no"
        valid_char = "[A-Za-z0-9_]"

        filename = self.filename_entry.get()
        # print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            # when space is entered its an error
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        # when nothing is entered it's a error
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        # print the problem message when there's an error
        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            # print()

        else:
            # if there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # heading for list
            f.write("EXPORTED JOB LIST\n" + "\n" + "*"*30)

            # add new line at end of each item
            for i in range(len(names)):
                f.write("\n   Job number: {} \n   Customer name: {} \n   Charge: ${:.2f}"
                        .format(i+1, names[i], charges[i]) + "\n" + "*"*30)

            # close file
            f.close()

            # close export box when click save button
            self.save_error_label.configure(text="Successfully saved", fg="green")
            self.filename_entry.configure(bg="light green")

    def close_export(self, partner):
        """
        when the close button on back button is pressed, indicating to exist out from export frame

        :return: export button on previous display frame in normal and destroys export_box
        """
        # Put export button back to normal
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Job_tracker()
    root.mainloop()
