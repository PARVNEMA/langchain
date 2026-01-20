from pydantic import BaseModel

# definee schema plus validation ''
class Student(BaseModel):
  name:str
  age:int


new_student ={'name':'parv','age':8}

student= Student(**new_student)

print(student)