import math #for use in calculations


#ask user what value they want to calculate

Variabletocalculate = str(input("What value would you like to calculate?"))
Variabletocalculate = Variabletocalculate.lower() #convert input to lowercase so easy to compare

#check which value the user inputted 
if Variabletocalculate == "initial velocity":
    
if Variabletocalculate == "final velocity":
    
if Variabletocalculate == "time taken":
    
if Variabletocalculate == "total distance travelled":
    
if Variabletocalculate == "tallest height reached":
    


def find initialvelocity(): #define a function to find the initial velocity and values the users has in order to find it
    Hasacceleration = str(input("Do you have value for acceleration(horizontal or vertical)? "))
    Hasacceleration = Hasacceleration.lower()
    if Hasacceleration == "yes":
        horizontalorverticalacceleration = str(input("Is the acceleration horizontal or vertical? "))
        horizontalorverticalacceleration = horizontalorverticalacceleration.lower()
        if horizontalorverticalacceleration == "horizontal":
            horizontalacceleration = float(input("Enter value of horizontal acceleration: "))
            Hastime = str(input("Do you have value for total time taken? "))
            Hastime = Hastime.lower()
            if Hastime == "yes":
                totaltime = float(input("Enter value of total time taken: "))
                Hasfinalhorizontalvelocity = str(input("Do you have value for horizontal final velocity? "))
                Hasfinalhorizontalvelocity = Hasfinalhorizontalvelocity.lower()
                if Hasfinalhorizontalvelocity == "yes":
                    finalhorizontalvelocity = float(input("Enter value of final horizontal velocity: "))
                    initialhorizontalvelocity = (finalhorizontalvelocity - (horizontalacceleration * totaltime))
                    Hasangle = str(input("Do you have value for angle of launch? "))
                    Hasangle = Hasangle.lower()
                    if Hasangle == "yes":
                        launchangle = float(input("Enter value of angle of launch: "))
                        initialvelocity = (initialhorizontalvelocity / math.cos(launchangle))
                    else:
                        Hasinitialverticalvelocity = str(input("Do you have value for vertical initial velocity? "))
                        Hasinitialverticalvelocity = Hasinitialverticalvelocity.lower()
                        if Hasinitialverticalvelocity == "yes":
                            initialverticalvelocity = float(input("Enter value of vertical initial velocity: "))
                            initialvelocity = math.sqrt((initialhorizontalvelocity **2) + (initialverticalvelocity **2))
                        else:
                            print("Not enough information provided.")
                else:
                    Hasfinalverticalvelocity = str(input("Do you have a value for vertical final velocity? "))
                    Hasfinalverticalvelocity = Hasfinalverticalvelocity.lower()
                    if Hasfinalverticalvelocity == "yes":
                        finalverticalvelocity = float(input("Enter value of vertical final velocity: "))
                        Hasverticalacceleration = str(input("Do you have value for vertical acceleration? "))
                        Hasverticalacceleration = Hasverticalacceleration.lower()
                        if Hasverticalacceleration == "yes":
                            verticalacceleration = float(input("Enter value of vertical acceleration: "))
                            initialverticalvelocity = (finalverticalvelocity - (verticalacceleration * totaltime))
                            Hasangle = str(input("Do you have value for angle of launch? "))
                            Hasangle = Hasangle.lower()
                            if Hasangle == "yes":
                                launchangle = float(input("Enter value of angle of launch: "))
                                initialvelocity = (initialverticalvelocity / math.sin(launchangle))
                            else:
                                Hasinitialhorizontalvelocity = str(input("Do you have value for horizontal initial velocity? "))
                                Hasinitialhorizontalvelocity = Hasinitialhorizontalvelocity.lower()
                                if Hasinitialhorizontalvelocity == "yes":
                                    initialhorizontalvelocity = float(input("Enter value of horizontal initial velocity: "))
                                    initialvelocity = math.sqrt((initialhorizontalvelocity **2) + (initialverticalvelocity **2))
                                else:
                                    print("Not enough information provided.")
                        else:
                            Hasverticaldisplacement = str(input("Do you have value for vertical displa"))
                            
                    

    else:
        