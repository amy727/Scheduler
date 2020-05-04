##Application Class
from tkinter import *
from tkinter import filedialog
from scheduler import *
from Schedule_class import*
from Exam_class import*
import os

global schedule, LOCATIONS, ofilename
ofilename = ""

#create schdule and availabilities
schedule = Schedule()
schedule.load_start_availabilities("availabilities.csv")

## List of locations
LOCATIONS = [
    "", "APSCDept-ComputerLab", "BA-1130", "BA-1160", "BA-1170", "BA-1180", "BA-2159", "BA-2165", "BA-2175",
    "BA-2185", "BA-2195", "BN-2N", "EX-100", "EX-200", "EX-300", "EX-310", "EX-320", "GB-303", "GB-304",
    "HA-316", "HA-401", "HA-403", "HA-410", "HI-CART", "MP-102", "MS-2172", "MS-3153", "MY-150", "MY-315",
    "MY-330", "MY-360", "MY-380", "SF-2202", "SF-3202", "WB-116", "WB-119", "WB-130", "WB-219", "WY-119",
    "ZZ-KNOX", "ZZ-VLAD"
]


class Application:
    
    """
    application class (GUI Interface)
    """

    def __init__(self, master):
        """
        Initialization of application
        Display inteface
        """      
        #Master
        self.master = master
        self.master.title("Spring 2020 Exam Scheduler")

        #top frame
        self.top_frame = Frame(self.master, background='grey22')
        self.top_frame.pack(expand=True)
        self.top_frame.columnconfigure(0, pad=10)
        self.top_frame.columnconfigure(1, pad=10)
        self.top_frame.columnconfigure(2, pad=10)
        self.top_frame.rowconfigure(0, pad=10)
        self.top_frame.rowconfigure(0, pad=10)
        self.top_frame.rowconfigure(0, pad=10)
        #self.top_frame.columnconfigure(2, pad=5)

        self.headerframe = LabelFrame(self.top_frame, bd=0)
        self.headerframe.grid(padx=20, pady=20, sticky="NSEW",columnspan=3)
        self.heading = Label(self.headerframe, text="\nSPRING 2020 EXAM SCHEDULER\n", font=('Helvetica',24)).pack()

        self.frame1 = LabelFrame(self.top_frame, width=60)
        self.frame1.grid(padx=20, pady=20, sticky="NSEW", rowspan=3, column=0)
        self.frame1.columnconfigure(0, pad=10)
        self.frame1.columnconfigure(1, pad=10)
        for i in range(11):
            self.frame1.rowconfigure(i, pad=5)

        self.frame2 = LabelFrame(self.top_frame, width=60)
        self.frame2.grid(padx=20, pady=20, sticky="NSEW", row=1, column=1)
        self.frame2.columnconfigure(0, pad=10)
        self.frame2.columnconfigure(1, pad=10)
        for i in range(11):
            self.frame2.rowconfigure(i, pad=5)

        self.frame3 = LabelFrame(self.top_frame, width=60)
        self.frame3.grid(padx=20, pady=20, sticky="NSEW", row=2, column=1)
        self.frame3.columnconfigure(0, pad=10)
        self.frame3.columnconfigure(1, pad=10)
        for i in range(11):
            self.frame3.rowconfigure(i, pad=5)

        self.frame4 = LabelFrame(self.top_frame, width=60)
        self.frame4.grid(padx=20, pady=20, sticky="NSEW", row=3, column=1)
        self.frame4.columnconfigure(0, pad=10)
        self.frame4.columnconfigure(1, pad=10)
        for i in range(11):
            self.frame4.rowconfigure(i, pad=5)

        self.frame5 = LabelFrame(self.top_frame, width=60)
        self.frame5.grid(padx=20, pady=20, sticky="NSEW", row=1, column=2)

        self.frame6 = LabelFrame(self.top_frame)
        self.frame6.grid(padx=20, pady=20, sticky="NSEW", row=2, rowspan=2, column=2)
        self.label6 = Label(self.frame6, text="SEARCH RESULT", anchor="center", justify="center", font=("Helvetica", 16), width=35)
        self.label6.pack(padx=20, pady=20)
        self.searchresult = Label(self.frame6, font=('Helvetica',10), background="white", width=55, height=20)
        self.searchresult.pack(padx=10,pady=10)

        #self.canvas=Canvas(self.frame5)
        
        ##UPLOAD Exam##############

        ##Label
        self.upload = Label(self.frame1, text="UPLOAD EXAM TO SCHEDULER", anchor="center", justify="center", font=("Helvetica", 16),width=35)
        self.upload.grid(padx=20, pady=20, row=0, columnspan = 2)

        ##Course code
        self.course_code_label = Label(self.frame1, text="Course Code", font=('Helvetica',12)).grid(row=1)
        self.course_code_entry = Entry(self.frame1, font=('Helvetica',12))
        self.course_code_entry.grid(row=1, column=1)

        ##Course name
        self.course_name_label = Label(self.frame1, text="Course Name", font=('Helvetica',12)).grid(row=2)
        self.course_name_entry = Entry(self.frame1, font=('Helvetica',12))
        self.course_name_entry.grid(row=2, column=1)

        ##Course Instructor
        self.instructor_label = Label(self.frame1, text="Course Instructor", font=('Helvetica',12)).grid(row=3)
        self.instructor_entry = Entry(self.frame1, font=('Helvetica',12))
        self.instructor_entry.grid(row=3, column=1)

        ##Class
        self.class_label = Label(self.frame1, text="Class Name", font=('Helvetica',12)).grid(row=4)
        self.class_entry = Entry(self.frame1, font=('Helvetica',12))
        self.class_entry.grid(row=4, column=1)

        ##Location
        self.location_label = Label(self.frame1, text="Preferred Exam Location", font=('Helvetica',12)).grid(row=5)
        self.l = StringVar(self.frame1)
        self.l.set("")
        self.location_entry = OptionMenu(self.frame1, self.l,*LOCATIONS)
        self.location_entry.grid(row=5, column=1)

        ##Start Time
        self.start_label = Label(self.frame1, text="Preferred Exam Start Time", font=('Helvetica',12)).grid(row=6)
        self.s = StringVar(self.frame1)
        self.s.set("")
        self.start_entry = OptionMenu(self.frame1, self.s, "", "9:30 AM", "2:00 PM", "6:30 PM")
        self.start_entry.grid(row=6, column=1) 

        ##Duration
        self.duration_label = Label(self.frame1, text="Exam Duration (in hours)", font=('Helvetica',12)).grid(row=7)
        self.d = StringVar(self.frame1)
        self.d.set("")
        self.duration_entry = OptionMenu(self.frame1, self.d, "", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0")
        self.duration_entry.grid(row=7, column=1)

        ##Priority
        self.priority_label = Label(self.frame1, text="Priority", font=('Helvetica',12)).grid(row=8)
        self.p = StringVar(self.frame1)
        self.p.set("")
        self.priority_entry = OptionMenu(self.frame1, self.p, "1", "2", "3")
        self.priority_entry.grid(row=8, column=1)

        ##upload
        self.upload_button = Button(self.frame1, text="Upload", command=self.upload_exam, font=('Helvetica',12)).grid(columnspan=2)

        ##Return message
        self.passLabel = Label(self.frame1, font=('Helvetica',12))
        self.passLabel.config(text="", font=('Helvetica',12))
        self.passLabel.grid(columnspan=2)


        ##### UPLOAD FILE ###########
        ##Label
        self.uploadfile = Label(self.frame2, text="UPLOAD FILE TO SCHEDULER", anchor="center", justify="center", font=("Helvetica", 16), width=35)
        self.uploadfile.grid(columnspan = 2, padx=20, pady=20)

        self.selectfile_button = Button(self.frame2, text="Select File to Schedule", command=self.select_file, font=('Helvetica',12)).grid(row=2, column = 0)
        self.fname = Label(self.frame2, bg="white", font=('Helvetica',10), width=30)
        self.fname.config(text="")
        self.fname.grid(row=2, column=1)
        self.uploadfile_button = Button(self.frame2, text="Upload File", command=self.upload_file, font=('Helvetica',12)).grid(column = 1)

        self.selectfile2_button = Button(self.frame2, text="Load previous Schedule", command=self.select_schedule, font=('Helvetica',12)).grid(row=5, column = 0)
        self.fname2 = Label(self.frame2, bg="white", font=('Helvetica',10), width=30)
        self.fname2.config(text="")
        self.fname2.grid(row=5, column=1)
        self.uploadfile2_button = Button(self.frame2, text="Load Schedule", command=self.upload_schedule, font=('Helvetica',12)).grid(column = 1)


        #### SEARCH EXAM ##########
        self.searchlabel = Label(self.frame3, text="SEARCH IN SCHEDULER", anchor="center", justify="center", font=("Helvetica", 16), width=35)
        self.searchlabel.grid(columnspan=2, padx=20, pady=20)
        self.searchlabel2 = Label(self.frame3, text="Enter course code or class name:", font=('Helvetica',12)).grid(columnspan=2)
        self.code = Entry(self.frame3, font=('Helvetica',12))
        self.code.grid(columnspan=2)
        self.search_button = Button(self.frame3, text="Enter", command=self.search, font=('Helvetica',12)).grid(column = 1)


        #### DELETE EXAM #########
        self.deletelabel = Label(self.frame4, text="DELETE EXAM FROM SCHEDULE", anchor="center", justify="center", font=("Helvetica", 16), width=35)
        self.deletelabel.grid(columnspan=2, padx=20, pady=20)
        self.deletelabel2 = Label(self.frame4, text="Enter course code:", font=('Helvetica',12)).grid(columnspan=2)
        self.delcode = Entry(self.frame4, font=('Helvetica',12))
        self.delcode.grid(columnspan=2)
        self.delete_button = Button(self.frame4, text="Enter", command=self.delete, font=('Helvetica',12)).grid(column = 1)
        self.deleteresult = Label(self.frame4, font=('Helvetica',12))
        self.deleteresult.grid(columnspan=2)


        ### SCHEDULE ########
        self.out = Label(self.frame5, text="SCHEDULE OUTPUT", anchor="center", justify="center", font=("Helvetica", 16),width=35).pack(padx=20, pady=20)
        self.output_button = Button(self.frame5, text="Output Schedule to CSV file", command=self.outputfile, font=('Helvetica',12), width=30).pack(pady=10)
        self.output_button = Button(self.frame5, text="Display Schedule in new window", command=self.outputdisplay, font=('Helvetica',12), width=30).pack(pady=10)
        self.outl = Label(self.frame5)
        self.outl.pack(pady=10)
        

    def upload_exam(self):
        """
        (self) -> str
        Gets entries from fields and returns them
        """

        course_code = self.course_code_entry.get().upper()
        course_name = self.course_name_entry.get()
        instructor = self.instructor_entry.get()
        class_name = self.class_entry.get().upper()
        location = self.l.get()
        duration = self.d.get()
        priority = self.p.get()
        start = self.s.get()

        if course_code == "" or course_name == "" or instructor == "" or class_name == "":
            self.passLabel.config(text="The following fields must be specified:\n-Course Code\n-Course Name\n-Course Instructor\n-Class Name")


        else:
            #Message to be displayed
            self.passLabel.config(text="Exam will be uploaded to scheduler")

            #Clear contents on GUI
            self.course_code_entry.delete(0, END)
            self.course_name_entry.delete(0, END)
            self.instructor_entry.delete(0, END)
            self.l.set("")
            self.d.set("")
            self.p.set("")
            self.class_entry.delete(0, END)
            self.s.set("")

            ##Parse contents to return
            if location == "":
                location = None

            if priority == "":
                priority = 3
            else:
                priority = int(priority)
            
            if duration == "":
                duration = 2.5
            else:
                duration = float(duration)
            
            if start == "":
                start_time = None
            elif start == "9:30 AM":
                start_time = 930
            elif start == "2:00 PM":
                start_time = 1400
            elif start == "6:30 PM":
                start_time = 1830

            print(course_code, course_name, instructor, location, duration, priority, class_name, start_time)
            exam = Exam(course_code, course_name, instructor, class_name, location, duration, priority, start_time)
            result = schedule.add_exam(exam)
            if result == 0:
                self.passLabel.config(text="A conflict occured\nExam cannot be scheduled")
            else:
                self.passLabel.config(text="An exam has been scheduled for " +exam.course_code+ "\non "+exam.date+ " at "+str(exam.start_time)+" in "+exam.location)

    def select_file(self):
        """
        (self) -> None
        When button is clicked, allows user to upload a file
        Changes text display to filename
        """

        self.filename = filedialog.askopenfilename(initialdir = "./", title="Select file", filetypes =(("CSV files","*.csv"),("Text files","*.txt"),("All files","*.*")))
        self.fname.config(text=self.filename)

    def upload_file(self):
        """
        (self) -> None
        Returns the filename that was selected
        """

        #upload_file
        filename = self.fname['text']
        print(filename)
        upload_file(filename, schedule)

        #reset text
        
        self.fname.config(text="File has been uploaded")

    def select_schedule(self):
        """
        (self) -> None
        When button is clicked, allows user to upload a file
        Changes text display to filename
        """

        self.filename = filedialog.askopenfilename(initialdir = "./", title="Select file", filetypes =(("CSV files","*.csv"),("Text files","*.txt"),("All files","*.*")))
        self.fname2.config(text=self.filename)

    def upload_schedule(self):
        """
        (self) -> None
        Returns the filename that was selected
        """

        #upload_file
        filename = self.fname2['text']
        print(filename)
        load_schedule(filename, schedule)

        #reset text
        self.fname2.config(text="Schedule has been loaded")

    def search(self):
        """
        (self) -> None
        """
        entry = self.code.get().upper()

        self.code.delete(0, END)

        print(entry)
        result = schedule.search_exam(entry) 
        result2 = schedule.search_class(entry)
        display = ""
        if result == None and len(result2) == 0:
            display = "There is no exam scheduled for " + entry
        elif result != None and len(result2) == 0:
            display = ("Course Code: " + result.course_code + "\n" + 
                "Course Name: " + result.course_name + "\n"
                + "Course Instructor: " + result.instructor + "\n"
                + "Exam Location: " + result.location + "\n"
                + "Exam Date: " + str(result.date) + "\n"
                + "Exam Start Time: " + str(result.start_time) + "\n")
        elif result == None and len(result2) != 0:
            display = "The exams scheduled for " +entry+ " are:\n\n"
            for exam in result2:
                display = display+ exam.course_code+ " on "+exam.date+ " at "+str(exam.start_time)+" in "+exam.location +"\n"
        self.searchresult.config(text=display)
        print(result)

    def delete(self):
        """
        (self) -> None
        """
        course_code = self.delcode.get().upper()

        self.delcode.delete(0, END)

        print(course_code)
        result = schedule.delete_exam(course_code) 

        if result == 1:
            self.deleteresult.config(text="Deletion Successful")
            print("Successful")
        else:
            self.deleteresult.config(text="There is no exam scheduled for the course")
            print("Unsucessful")

    def outputfile(self):
        """
        outputs scheduled file
        """
        #global self.ofilename 
        self.filename = filedialog.asksaveasfilename(initialdir = "./", title="Save as file", filetypes =(("CSV files","*.csv"),("Text files","*.txt"),("All files","*.*")))
        
        #output schedule to two different csv files
        output(self.filename, schedule) #this can be uploaded to the calendar
        output_scheduler(self.filename[:-4]+"_scheduler_file.csv", schedule)
        self.outl.config(text="Output successful")
    
    def outputdisplay(self):
        #open new window
        self.newWindow = Toplevel(self.master)
        self.app = Application2(self.newWindow)

class Application2:

    def __init__(self, master):
        """
        Schedule Display window
        """
        #Master
        self.master = master
        self.master.title("Spring 2020 Exam Scheduler")

        #top frame
        self.frame = Frame(self.master, background='grey22')
        self.frame.pack()

        self.headerframe = LabelFrame(self.frame, bd=0)
        self.headerframe.pack(padx=30, pady=30)
        self.heading = Label(self.headerframe, text="\nSPRING 2020 EXAM SCHEDULE DETAILS\n", font=('Helvetica',24)).pack(padx=20, pady=20)

        #self.f = Button(self.top_frame, text="Select Scheduler file to Display", command=self.displayoutput, font=('Helvetica',12)).grid(pady=20, columnspan=2)

        self.frame2 = Frame(self.frame)
        self.frame2.pack(pady=20,padx=20)
        
        self.canvas = Canvas(self.frame2, background='grey22', width=640)
        self.myscrollbar = Scrollbar(self.frame2, orient="vertical", command=self.canvas.yview)
        self.outputlist = Frame(self.canvas)
        #self.outputlist.pack()

        self.outputlist.bind(
            "<Configure>", 
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0,0), window=self.outputlist, anchor="nw")
        self.canvas.configure(yscrollcommand = self.myscrollbar.set)

        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="right", fill="both", expand=True)
        
        self.displayoutput()


    def displayoutput(self):
        """
        displays contents of csv file
        """

        #header
        self.label = Label(self.outputlist, text="Class", font=('Helvetica',12)).grid(row=0, column=0, padx=5, pady=5)
        self.label = Label(self.outputlist, text="Course code", font=('Helvetica',12)).grid(row=0, column=1, padx=5, pady=5)
        self.label = Label(self.outputlist, text="Exam Date", font=('Helvetica',12)).grid(row=0, column=2, padx=5, pady=5)
        self.label = Label(self.outputlist, text="Start Time", font=('Helvetica',12)).grid(row=0, column=3, padx=5, pady=5)
        self.label = Label(self.outputlist, text="End Time", font=('Helvetica',12)).grid(row=0, column=4, padx=5, pady=5)
        self.label = Label(self.outputlist, text="Location", font=('Helvetica',12)).grid(row=0, column=5, padx=5, pady=5)
        self.label = Label(self.outputlist, text="Overload", font=('Helvetica',12)).grid(row=0, column=6, padx=5, pady=5)

        classes = schedule.ClassList
        #print(exams)

        colours=['PaleTurquoise1', 'lemon chiffon', 'thistle', 'DarkSeaGreen1']

        i = 1
        j = 1
        for c in classes:

            for course in classes[c]:

                code = course[1]

                exam = schedule.ExamList[code]
                print(exam)

                ##parsing exam info
                course_code = exam.course_code
                location = exam.location
                duration = exam.duration

                if exam.overload == True:
                    colour1 = 'RosyBrown1'
                    overload = "Overloaded"
                else:
                    colour1 = colours[j%4]
                    overload = "          "
                
                start_time = exam.start_time
                if(start_time==930): 
                    start = "9:30 AM"
                    end_h = int(9.5+duration)
                    end_m = int((9.5+duration - end_h)*60)
                elif(start_time==1400):
                    start = "2:00 PM"
                    end_h = int(14+duration)
                    end_m = int((14+duration - end_h)*60)
                elif(start_time==1830):
                    start = "6:30 PM"
                    end_h = int(18.5+duration)
                    end_m = int((18.5+duration - end_h)*60)

                if(end_h == 12 and len(str(end_m))==1):
                    end = str(end_h)+":0"+str(end_m)+" PM"
                elif(end_h < 12 and len(str(end_m))==1):
                    end = str(end_h)+":0"+str(end_m)+" AM"
                elif(end_h < 12 and len(str(end_m))==2):
                    end = str(end_h)+":"+str(end_m)+" AM"
                elif(end_h > 12 and len(str(end_m))==1):
                    end = str(end_h-12)+":0"+str(end_m)+" PM"
                else:
                    end = str(end_h-12)+":"+str(end_m)+" PM"
                
                class_name = exam.class_name

                month = exam.date.split("-")[0]
                day = exam.date.split("-")[1]
                date = month + "/" + day +"/2020"

                self.label = Label(self.outputlist, text=class_name, bg=colour1).grid(row=i, column=0, padx=5, pady=5)
                self.label = Label(self.outputlist, text=course_code, bg=colour1).grid(row=i, column=1, padx=5, pady=5)
                self.label = Label(self.outputlist, text=date, bg=colour1).grid(row=i, column=2, padx=5, pady=5)
                self.label = Label(self.outputlist, text=start, bg=colour1).grid(row=i, column=3, padx=5, pady=5)
                self.label = Label(self.outputlist, text=end, bg=colour1).grid(row=i, column=4, padx=5, pady=5)
                self.label = Label(self.outputlist, text=location, bg=colour1).grid(row=i, column=5, padx=5, pady=5)
                self.label = Label(self.outputlist, text=overload, bg=colour1).grid(row=i, column=6, padx=5, pady=5)

                i+=1

            j+=1
