from src.calss_person import Person


class Student(Person):

    def __init__(self, name=None, family=None, id=None, GPA=None, status=None):
        Person.__init__(self, name, family, id)

        self.GPA = GPA
        self.status = status
    
    def __repr__(self) -> str:


        return f'{self.__class__.__name__} {self.name}  {self.family} {self.id} your GPA is{self.GPA} and you are {self.status}'

    def take_cours(self):

        #recive the courses that the student want to pick
        #then make it to a dictionary with zero values

        courses = input('please enter the corses you want sep with space:')

        courses = dict(map(lambda x:(x,0) , courses.split(' ')))

        return courses

