import os 
import json
file_path = os.path.abspath("course_json.json")

def json_writer(course):

    with open(file_path,'a') as write:
        
        json.dump(course, write)