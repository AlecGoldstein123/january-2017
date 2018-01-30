"""a=0
while a in range (100000000):
    milesdriven= float(input("How many miles have you driven?: "))
    gallonsused= float(input("How many gallons have you used?: "))
    mpg= float(milesdriven / gallonsused)
    print("Your car uses", mpg ,"per gallon.")
    yesorno=input("Do you want to continue?: ")
    if yesorno=="no":
        break"""
"""
while True:
    print("This program calculates mpg.")
    milesdriven= float(input("How many miles have you driven?: "))
    gallonsused= float(input("How many gallons have you used?: "))
    mpg= float(milesdriven / gallonsused)
    print("Your car uses", mpg ,"per gallon.")
    yesorno=input("Do you want to continue? (yes/no): ")
    if yesorno== "yes" or yesorno== "Yes":
        continue
    else:
        break
    """

while True:
    print("This program calculates area of rectangle.")
    length = float(input("What is the length of your rectangle?: "))
    width = float(input("What is the width of your rectangle?: "))
    area = float(length * width)
    print("The area is:",area)
    hi= input("Would you like to try again, yes or no?: ") 
    if hi== "yes" or hi=="Yes":
        continue
    else:
        break
    
