#Scheduler Functions

from Schedule_class import*
from Exam_class import*

### UPLOAD File ####
def upload_file(filename, schedule):
    """
    (str, Schedule) -> None

    Creates a schedule from the uploaded file
    """

    #open file
    file = open(filename, 'r')

    i = 0
    for line in file:
        
        if i != 0:

            #get info
            info = line.split(",")

            #parse info
            code = info[0].rstrip()
            name = info[1].rstrip()
            instructor = info[2].rstrip()
            location = info[3].rstrip()
            duration = float(info[4].rstrip())
            priority = int(info[5].rstrip())
            class_name = info[6].rstrip()

            #create Exam object
            exam = Exam(code, name, instructor, class_name, location, duration, priority)
            print(exam)

            #add to schedule
            print(schedule.add_exam(exam))


        i += 1

    #close file
    file.close()


##OUTPUT FILE
def output(filename, schedule):
    """
    (str, Schedule) -> None
    prints schedule to a file called filename
    """
    file = open(filename, "w")

    #header
    file.write("Subject,Start Date,Start Time,End Date,End Time,Location,Description\n")

    classes = schedule.ClassList
    #print(exams)

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
                overload = "Overloaded"
            else:
                overload = ""
            
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
            subject = "Class " + class_name + " - " + course_code

            month = exam.date.split("-")[0]
            day = exam.date.split("-")[1]
            date = month + "/" + day +"/2020"

            file.write(subject+","+date+","+start+","+date+","+end+","+location+","+overload+"\n")

    file.close()

##OUTPUT FILE
def output_scheduler(filename, schedule):
    """
    (str, Schedule) -> None
    prints schedule to a file called filename
    """
    file = open(filename, "w")

    #header
    file.write("Course Code,Course Name,Course Instructor,Class Name,Location,Duration,Priority,Start Time,Date,Overload\n")

    classes = schedule.ClassList
    #print(exams)

    for c in classes:

        for course in classes[c]:

            code = course[1]

            exam = schedule.ExamList[code]
            print(exam)
            if exam.overload == False:
                overload = "0"
            else:
                overload="1"

            file.write(exam.course_code+","+exam.course_name+","+exam.instructor+","+exam.class_name+","
                +exam.location+","+str(exam.duration)+","+str(exam.priority)+","+str(exam.start_time)+","
                +exam.date+","+overload+"\n")

    file.close()


def load_schedule(filename, schedule):
    """
    (str, Schedule) -> None
    updates schedule with already scheduled courses
    """

    file = open(filename, "r")

    i = 0
    for line in file:

        if i != 0:
            info = line.split(",")

            #parse info
            code = info[0].rstrip()
            name = info[1].rstrip()
            instructor = info[2].rstrip()
            class_name = info[3].rstrip()
            location = info[4].rstrip()
            duration = float(info[5].rstrip())
            priority = int(info[6].rstrip())
            start = int(info[7].rstrip())
            date = info[8].rstrip()
            overload = int(info[9].rstrip())
            

            #create Exam object
            exam = Exam(code, name, instructor, class_name, location, duration, priority, start)
            print(exam)

            #add to schedule
            exam.date = date
            index = schedule.indexes[date+"-"+str(start)]
            exam.index = index
            if overload == 1:
                exam.overload = True

            #add exam to ExamList
            schedule.ExamList[exam.course_code] = exam

            #add exam to ClassList
            if (exam.class_name in schedule.ClassList):
                schedule.ClassList[exam.class_name].append((index, exam.course_code, location))
            else:
                schedule.ClassList[exam.class_name] = [(index, exam.course_code, location)]
            

            #add exam to availabilities
            schedule.availabilities[index][1][location] = 0
            #add one to num exams
            schedule.num_exams += 1
            print(schedule.add_exam(exam))


        i += 1
        

    file.close()




