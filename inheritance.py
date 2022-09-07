

class Domestic ():
    def aboutme(self):
        print("I am a domestic anaimal")



class Mamals():
    
    def walk(self):
        print("I can walk")


class Cat(Mamals,Domestic) :
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place



    

class Dog(Mamals,Domestic) :
    x=0
    
class Tiger(Mamals) :
    x=0

myavu=Cat("rajappan",12,"arookutty") 
tinku=Cat("tinku",12,"Thiruvankulam")
myavu.walk()

print(myavu.name)
print(myavu.age)
print(myavu.place)

myavu.aboutme()
    


    
