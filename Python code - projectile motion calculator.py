#ask user what value they want to calculate
Variabletocalculate = str(input("What value would you like to calculate?"))
Variabletocalculate = Variabletocalculate.lower() #convert input to lowercase so easy to compare
#ask user to enter value for this variable
valuetocalculate = float(input("Enter value for " + Variabletocalculate + ": "))


#check which value the user inputted and store that value in a variable
if Variabletocalculate == "initial velocity":
    initialvelocity = valuetocalculate
if Variabletocalculate == "final velocity":
    finalvelocity = valuetocalculate
if Variabletocalculate == "time taken":
    timetaken = valuetocalculate
if Variabletocalculate == "total distance travelled":
    totaldistance = valuetocalculate
if Variabletocalculate == "tallest height reached":
    tallestheight = valuetocalculate