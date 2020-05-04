## MAIN

from Application_class import *    

if __name__ == "__main__":
    
    """
    Main function
    """
    root = Tk()
    #root.minsize(600, 400)
    #root.maxsize(1200, 1000)
    root.resizable(False, False)
    #root.configure(bg='ivory2')

    app = Application(root)

    root.mainloop()
    

    #exam = Exam('AER210H1','Vector Calc. & Fluid Mechanics', 'Pauline Ledbetter', 23, 'MY-315',2.5,1,930)
    #exam2 = Exam('AER210H2','Vector Calc. & Fluid Mechanics', 'Pauline Ledbetter', 23,'MY-315',2.5,1,930)

    #print(s.add_exam(exam))
    #print(s.add_exam(exam2))

    #upload_file("eng_exam.csv", s)

    #print(s.search_exam('AER210H1'))
    #print(s.delete_exam('AER210H1'))
    #print(s.search_exam('AER210H1'))

    #output("schedule.csv", s)
