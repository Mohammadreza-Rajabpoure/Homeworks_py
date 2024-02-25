from src.calss_person import Person

class Professor(Person):

    def __init__(self, name=None, family=None, id=None, courses=None):
        Person.__init__(self, name, family, id)

        self.courses = courses
   
    def __repr__(self) -> str:
        return f'{__class__.__name__} {self.name} {self.family} {self.id}'
    
    
    def give_grade(self, course_names:dict):#put the grades for courses that the student taked

        for course in course_names:
            
            x=float(input(f'pleas enter the grade {course} :'))

            course_names[course] = x
        
        return course_names