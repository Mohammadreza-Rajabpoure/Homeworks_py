from src.MyError import MyError

def inp():

    name = (input('please enter your first name:')).capitalize()

    family = (input('please enter your last name:')).capitalize()

    try:
          
        id = int(input('pleas enter your id:'))
    
        if id not in range(10000,100000):
           raise MyError(id)
    
    except  MyError as te :
       print(te)
    
    info_list = [name, family, id]

    return info_list