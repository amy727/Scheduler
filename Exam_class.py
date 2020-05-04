#Exam class

class Exam:

    def __init__(self, course_code, course_name, instructor, class_name, location=None, duration=2.5, priority=3, start_time=None):
        """
        (str, str, str, str, float, int, str, int) -> None

        course_code: string - course code of the exam (has to be specified)
        course_name: string - location of the exam (has to be specified)
        instructor: string - name of course instructor (has to be specified)
        class_name: integer - has to be specified
        location: string - location of exam (if not specified it will be None)
        start_time: int - start of the exam given in hours (e.g. 6:30pm would be represented as 1830) (if not specified it will be None)
        duration: float - duration of the exam in hours (if not specified it will be 2.5 hours)
        priority: integer of values 1, 2 or 3 (1 being highest priority) - priority of the exam (if not specified, is set as 3)
        date: string - mm-dd
        index: int - datetime of the exam
        overload: bool - True if class with exam is overloaded
        """
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor 
        self.location = location
        self.start_time = start_time
        self.duration = duration
        self.priority = priority
        self.class_name = class_name
        self.date = ""
        self.index = 0
        self.overload = False

    def __str__(self):
        message = "The exam for "+ str(self.course_code) +" "+ str(self.course_name) +" starts at "+ str(self.start_time) +" on "+ str(self.date) +" in "+str(self.location) 
        return message



        



