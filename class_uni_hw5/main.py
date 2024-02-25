''''project: made a class of person(superclass) then made two classes (student and professor),
    
     that they are subclasses of class person ,
     first we get the informations of the student and the courses he/she want
     then made a dictionary of courses with value 0 and write it to a json file as an object
     after that we get informations of professor
     then shows him/her the corses that as an dict and iterate the dict to input the grades
     after that we compute the GPA and status of student 
     and update the student attribiutes and shows the student object at last '''


from src.calss_person import Person

from src.class_professor import Professor

from src.class_student import Student

from statistics import mean

from src.user_info import inp

from src.show_courses import show_cours

from src.json_writer import json_writer

import json
import os

def main():
    
    print('Please enter student information')

    st_info=inp()#get information of student that info returns alist[name,family,id]
        
    name=st_info[0]

    family=st_info[1]

    id=st_info[2]

    student=Student(name,family,id) #made a student object

    show_cours()    #show courses to the student

    studen_pick = student.take_cours()

    json_writer(studen_pick)     #write the dictionary of studen_pick in json file

    print('please enter professor information')

    pro_info = inp() #get information of professor to make an object of professor

    name_pro = pro_info[0]
    family_pro = pro_info[1]
    id_pro = pro_info[2]

    professor_ = Professor(name_pro, family_pro, id_pro)

    file_path = os.path.abspath("course_json.json")

    with open(file_path ) as read:

        subjects = json.load(read)

        print(subjects)  #show the courses to professor for giving grades

        final_dict = professor_.give_grade(subjects)

        values = final_dict.values()

        GPA = mean(values)  #set the GPA for student

        student.GPA = GPA
        if GPA > 10 :      #set status for student

            student.status = 'pass'
        elif GPA < 10:
            student.status = 'faile'
        else:
            print('the mean must be in range (0,20)')


        print(student)


main()
