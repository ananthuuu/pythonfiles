option=input("""Please Select the required operation from the list

1) Addition
2) Subtraction
3) Division
4) Multiplication
5) Remainder
6) Power


""")
x=input("Please enter the the First numbers")
y=input("Please enter the the Second numbers")

x=float(x)
y=float(y)

if(option=="1") :
    print("The option selected is Addition")
    sum=x+y 
    print(f"The sum of the {x} and {y} is {sum}")

elif(option=="2") :
    print("The option selected is Subtraction")
    difference=x-y 
    print(f"The sum of the {x} and {y} is {difference}")

elif(option=="3") :
    print("The option selected is division")
    division=x/y 
    print(f"The division of the {x} and {y} is {division}")

elif(option=="4") :
    print("The option selected is Product")
    product=x*y 
    print(f"The Product of the {x} and {y} is {product}")

elif(option=="5") :
    print("The option selected is Remainder")
    remainder=x%y 
    print(f"The remainder of the {x} and {y} is {remainder}")

elif(option=="6") :
    print("The option selected is Power")
    power=x**y 
    print(f"The Exponential result of the {x} and {y} is {power}")

else :
    print("Please select a valid operation")

    




