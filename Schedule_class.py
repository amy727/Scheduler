#Schedule Class

class Schedule:

    def __init__(self):
        """
        Initializes new Schedule

        availabilities = dict{index: (mm-dd-time, {location: availability})}
        ExamList = dict{course_name: Exam}
        ClassList = dict{class_name: [(index, course_code, location)] }
        num_exams = int
        first_p2 = int
        last_p2 = int
        """
        self.availabilities = {} 
        self.ExamList = {}
        self.ClassList = {}
        self.num_exams = 0
        self.first_p2 = 10 #datetime of first 2nd priority exam
        self.last_p2 = 19 #datetime of last 2nd priority exam
        self.indexes = {
            "04-14-930":1, "04-14-1400":2, "04-14-1830":3, "04-15-930":4, "04-15-1400":5, "04-15-1830":6,
            "04-16-930":7, "04-16-1400":8, "04-16-1830":9, "04-17-930":10, "04-17-1400":11, "04-17-1830":12,
            "04-18-930":13, "04-18-1400":14, "04-18-1830":15, "04-20-930":16, "04-20-1400":17, "04-20-1830":18,
            "04-21-930":19, "04-21-1400":20, "04-21-1830":21, "04-22-930":22, "04-22-1400":23, "04-22-1830":24,
            "04-23-930":25, "04-23-1400":26, "04-23-1830":27, "04-24-930":28, "04-24-1400":29, "04-24-1830":30,
            "04-25-930":31, "04-25-1400":32, "04-25-1830":33, "04-27-930":34, "04-27-1400":35, "04-27-1830":36,
            "04-28-930":37, "04-28-1400":38, "04-28-1830":39
        }

    
    ##Loading beginning availabilities
    def load_start_availabilities(self, filename):
        """
        Loads availabilities from file with filename
        
        In the format of:
        {day: (mm-dd-time, {location: availability})}

        where:
            day = an integer starting from 1 (ie the first exam date is day 1)
            mm-dd-time = month-day-24hour time format (ie 1830)
            location = room
            availability = 1 if available, either a 0 or an exam if not available
        """

        #open file
        file = open(filename, 'r')

        #parse through file
        i = 0
        for line in file: #read through lines
            
            #split line
            info = line.split(",")
            
            if i==0: #get date-time
                for j in range(len(info)):
                    if j!=0:
                        self.availabilities[j] = (info[j].rstrip(), {})

            else: #get location and availability
                location = ""
                for j in range(len(info)):
                    if j==0:
                        location = info[j]
                    else:
                        self.availabilities[j][1][location] = (int) (info[j].rstrip())

            i += 1

        #print(self.availabilities)
        #close file
        file.close()

    
    ##Schedule exam based on availabilities
    def add_exam(self, exam):
        """
        (Exam, Schedule) -> int
        Returns 1 if successful
        Returns 0 if conflict occurs
        """

        #variables
        priority = exam.priority #priority of exam
        location = exam.location #location
        start_time = exam.start_time  #start_time

        if(priority==1):
            start = 1
            end = self.first_p2
        elif(priority==2):
            start = self.first_p2
            end = self.last_p2
        elif(priority==3):
            start = self.last_p2
            end = 39

        if(start_time==930):
            start = start
        elif(start_time==1400):
            start = start + 1
        elif(start_time==1830):
            start = start + 2


        print(exam)

        #=========BOTH LOCATION AND START TIME ARE KNOWN =================
        if (location!= None) and (start_time!=None):

            for i in range(start, end+1, 3):

                if self.availabilities[i][1][location] == 1: #check if location is available

                    #check conflict or overload
                    if (self.check_conflict(exam, i) == 0):

                        #update start time of exam
                        datetime = self.availabilities[i][0]
                        time = datetime.split("-")
                        exam.start_time = (int) (time[2])
                        exam.date = time[0] + "-" + time[1]
                        exam.index = i

                        #add exam to ExamList
                        self.ExamList[exam.course_code] = exam

                        #add exam to ClassList
                        if (exam.class_name in self.ClassList):
                            self.ClassList[exam.class_name].append((i, exam.course_code, location))
                        else:
                            self.ClassList[exam.class_name] = [(i, exam.course_code, location)]
                        

                        #add exam to availabilities
                        self.availabilities[i][1][location] = 0
                        #add one to num exams
                        self.num_exams += 1
                        print(exam)

                        return 1

            #conflict
            print("Conflict occured - will reschedule with different time")
            exam.start_time = None
            return self.add_exam(exam)
                            

        #=========ONLY LOCATION IS KNOWN =================
        elif (location!= None) and (start_time == None):

            for i in range(start, end+1):

                if self.availabilities[i][1][location] == 1: #check if location is available

                    #check conflict or overload
                    if (self.check_conflict(exam, i) == 0):
                        #update date, time and location of exam
                        datetime = self.availabilities[i][0]
                        time = datetime.split("-")
                        exam.start_time = (int) (time[2])
                        exam.date = time[0] + "-" + time[1]
                        exam.location = location
                        exam.index = i

                        #add exam to ClassList
                        if (exam.class_name in self.ClassList):
                            self.ClassList[exam.class_name].append((i, exam.course_code, location))
                        else:
                            self.ClassList[exam.class_name] = [(i, exam.course_code, location)]

                        #print(self.ClassList)

                        #add exam to ExamList
                        self.ExamList[exam.course_code] = exam

                        #add exam to availabilities
                        self.availabilities[i][1][location] = 0
                        #add one to num exams
                        self.num_exams += 1

                        return 1

            #If conflict occurs        
            print("Conflict occured- will reschedule with different location")
            exam.location = None
            return self.add_exam(exam)


        #=========ONLY START TIME IS KNOWN =================
        elif (start_time != None):

            for i in range(start, end+1, 3):

                for location in self.availabilities[i][1]: #check for availability

                    #check availability
                    if self.availabilities[i][1][location] == 1: 

                        #check conflict or overload
                        if (self.check_conflict(exam, i) == 0):

                            #update time and location of exam
                            datetime = self.availabilities[i][0]
                            time = datetime.split("-")
                            exam.start_time = (int) (time[2])
                            exam.date = time[0] + "-" + time[1]
                            exam.location = location
                            exam.index = i

                            #add exam to ExamList
                            self.ExamList[exam.course_code] = exam

                            #add exam to ClassList
                            if (exam.class_name in self.ClassList):
                                self.ClassList[exam.class_name].append((i, exam.course_code, location))
                            else:
                                self.ClassList[exam.class_name] = [(i, exam.course_code, location)]
                            

                            #add exam to availabilities
                            self.availabilities[i][1][location] = 0
                            #add one to num exams
                            self.num_exams += 1
                            print(exam)

                            return 1

            #if conflict occurs
            print("conflict - will reschedule with different start time")
            exam.start_time = None
            return self.add_exam(exam)
                            

        #========= LOCATION AND START TIME BOTH HAVE NOT BEEN SPECIFIED =================
        else:

            for i in range(start, end+1):

                for location in self.availabilities[i][1]: #check for availability

                    #check availability
                    if self.availabilities[i][1][location] == 1:

                        conflict = self.check_conflict(exam, i)

                        #check conflict or overload
                        if (conflict < 2):

                            #update date, time and location of exam
                            datetime = self.availabilities[i][0]
                            time = datetime.split("-")
                            exam.start_time = (int) (time[2])
                            exam.date = time[0] + "-" + time[1]
                            exam.location = location
                            exam.index = i

                            if(conflict==1):
                                exam.overload = True

                            #add exam to ExamList
                            self.ExamList[exam.course_code] = exam

                            #add exam to ClassList
                            if (exam.class_name in self.ClassList):
                                self.ClassList[exam.class_name].append((i, exam.course_code, location))
                            else:
                                self.ClassList[exam.class_name] = [(i, exam.course_code, location)]
                            

                            #add exam to availabilities
                            self.availabilities[i][1][location] = 0
                            #add one to num exams
                            self.num_exams += 1
                            print(exam)

                            return 1

            #if conflict occurs
            print("Priority conflict cannot be resolved")
            return 0


    #Check if class is overloaded
    def check_conflict(self, exam, index):
        """
        (Exam) -> int

        Returns 1 if there is an overload
        Returns 2 if there is a conflict (same time same class)
        Returns 0 if not overloaded
        """

        class_name = exam.class_name

        #if class is in ClassList
        if class_name in self.ClassList:

            datetimes = self.ClassList[class_name]
            print(datetimes, index)

            #if index already exists
            for i in range(len(datetimes)):
                if (datetimes[i][0]==index):
                    return 2

            datetimes.sort()
            #Check if there exists an overload at specified index
            #check 2 datetimes at a time 
            for i in range(len(datetimes)-1):

                #check range of datetimes -> should be more than 9 sections
                if (datetimes[i+1][0] - datetimes[i][0] <= 9): 

                    #if their range is less than 9 sections -> index cannot be within those 9 sections
                    #if index is between them or is one of them:
                    if(index >= datetimes[i][0] and index <= datetimes[i][0]+9):
                        
                        return 1 #overloaded
        

        return 0

        
    #Delete exam
    def delete_exam(self, course_name):
        """
        (str) -> int

        Deletes exam from scheduler
        Returns 1 if deletion is successful
        Returns 0 if deletion fails
        """

        if course_name in self.ExamList:
            exam = self.ExamList[course_name]
            datetime = exam.index
            location = exam.location
            class_name = exam.class_name

            ##Remove from availability -> switch to 1
            self.availabilities[datetime][1][location] = 1

            ##delete exam from ExamList
            del(self.ExamList[course_name])

            ##delete exam from ClassList
            self.ClassList[class_name].remove((datetime, course_name, location))

            self.num_exams -= 1

            return 1

        else:
            print("Course does not exist")
            return 0


    #Search Exam
    def search_exam(self, course_code):
        """
        (str) -> Exam
        Returns an exam with the specified its course code
        """
        if course_code in self.ExamList:
            exam = self.ExamList[course_code]
            return exam
        else:
            return None

    def search_class(self, class_name):
        """
        (str) -> list of exams
        """

        exams = []

        if class_name in self.ClassList:

            for course in self.ClassList[class_name]:

                code = course[1]
                exam = self.ExamList[code]
                exams.append(exam)

        return exams

    


        



