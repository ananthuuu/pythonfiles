from curses.ascii import NUL


def sum (x,y):
    print( x+y )
    
def namegenerator(firstname,lastname="") :
    fullname=f"{firstname}  {lastname}"
    list=[1,2,4,5]

    returndictionary={}
    

    returndictionary["fullname"]=fullname
    returndictionary["firstname"]=firstname
    returndictionary["lastname"]=lastname
    returndictionary["list"]=list
    return returndictionary


mydictionary=namegenerator("Ananth","C jayan")
print(mydictionary["list"])





