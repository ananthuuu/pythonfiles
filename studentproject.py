



class Person():
    def __init__(self,name,age,location):
        self.name=name
        self.age=age 
        self.location=location

class Academic():
    def __init__(self,school,mathsmark,sciencemark):
        self.school=school
        self.mathsmark=mathsmark 
        self.sciencemark=sciencemark
        self.averagemark=(float(mathsmark)+float(sciencemark))/2


count=int(input(" Please Enter the Number of students : "))

i=0 








while(i<count):
    
    i=i+1
    name=input("Please Enter name")
    age=input("Please Enter age")
    location=input("Please Enter location")
    school=input("Please Enter school")
    mathsmark=input("Please Maths mark ")
    sciencemark=input("Please Science Mark")
    x=Person(name,age,location)
    y=Academic(school,mathsmark,sciencemark)

    print( f""" TheStudent Name is {x.name} 
    The Student Age is {x.age}
    The Student location is {x.location}
    The Student school is {y.school}
    The Student mathmark is {y.mathsmark}
    The Student sciencemark is {y.sciencemark}
    The Student Average Mark is {y.averagemark}
    """)

















    






