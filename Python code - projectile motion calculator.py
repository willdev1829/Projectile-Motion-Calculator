import math #for use in calculations
Horizontalcounter = 0 #counts number of horizontal values provided
Verticalcounter = 0 #counts number of vertical values provided

Hashorizontaldisplacement = str(input("Do you have value for horizontal displacement? "))
Hashorizontaldisplacement = Hashorizontaldisplacement.lower()
if Hashorizontaldisplacement == 'yes':
    Horizontalcounter = Horizontalcounter + 1
    horizontaldisplacement = float(input("Enter value of horizontal displacement: "))
    
Hashorizontalinitialvelocity = str(input("Do you have value for horizontal initial velocity? "))
Hashorizontalinitialvelocity = Hashorizontalinitialvelocity.lower()
if Hashorizontalinitialvelocity == 'yes':
    Horizontalcounter = Horizontalcounter + 1
    horizontalinitialvelocity = float(input("Enter value of horizontal initial velocity: "))

Hashorizontalfinalvelocity = str(input("Do you have value for horizontal final velocity? "))
Hashorizontalfinalvelocity = Hashorizontalfinalvelocity.lower()
if Hashorizontalfinalvelocity == 'yes':
    Horizontalcounter = Horizontalcounter + 1
    horizontalfinalvelocity = float(input("Enter value of horizontal final velocity: "))
    
Hashorizontalacceleration = str(input("Do you have value for horizontal acceleration? "))
Hashorizontalacceleration = Hashorizontalacceleration.lower()
if Hashorizontalacceleration == 'yes':
    Horizontalcounter = Horizontalcounter + 1
    horizontalacceleration = float(input("Enter value of horizontal acceleration: "))
    
Hastotaltime = str(input("Do you have value for total time? "))
Hastotaltime = Hastotaltime.lower()
if Hastotaltime == 'yes':
    Horizontalcounter = Horizontalcounter + 1
    Verticalcounter = Verticalcounter + 1
    totaltime = float(input("Enter value of total time: "))
    
Hasverticaldisplacement = str(input("Do you have value for vertical displacement? "))
Hasverticaldisplacement = Hasverticaldisplacement.lower()
if Hasverticaldisplacement == 'yes':
    Verticalcounter = Verticalcounter + 1
    verticaldisplacement = float(input("Enter value of vertical displacement: "))
    
Hasverticalinitialvelocity = str(input("Do you have value for vertical initial velocity? "))
Hasverticalinitialvelocity = Hasverticalinitialvelocity.lower()
if Hasverticalinitialvelocity == 'yes':
    Verticalcounter = Verticalcounter + 1
    verticalinitialvelocity = float(input("Enter value of vertical initial velocity: "))

Hasverticalfinalvelocity = str(input("Do you have value for vertical final velocity? "))
Hasverticalfinalvelocity = Hasverticalfinalvelocity.lower()
if Hasverticalfinalvelocity == 'yes':
    Verticalcounter = Verticalcounter + 1
    verticalfinalvelocity = float(input("Enter value of vertical final velocity: "))
    
Hasverticalacceleration = str(input("Do you have value for vertical acceleration? "))
Hasverticalacceleration = Hasverticalacceleration.lower()
if Hasverticalacceleration == 'yes':
    Verticalcounter = Verticalcounter + 1
    verticalacceleration = float(input("Enter value of vertical acceleration: "))

def calculateinitialvelocity(): #define function to calculate initial velocity
    if Horizontalcounter < 3 and Verticalcounter < 3: #if less than 3 values of horizontal or vertical motion given, impossible to calculate initial velocity
        print("Not enough information provided")
        exit()
    Hasangle = str(input("Do you have angle of projection?: ")) #check where user has angle of projection
    Hasangle = Hasangle.lower()
    if Hasangle == 'yes':
        projectionangle = float(input("Enter value of angle of projection: "))
        projectionangle = math.radians(projectionangle) #converts angle from degrees to radians for use in trigonometry calculations
        velocitytype = 'singular' #calculator will use trigonometry to calculate initial velocity
    else:
        velocitytype = 'both' #calculator will use pythagoras theorem to calculate initial velocity
    if velocitytype == 'singular': #code for calculating initial horizontal OR vertical velocity.
        if Horizontalcounter > 2:
            if Hastotaltime != 'yes': #no time value, so uses suvat equation which doesn't involve time.
                horizontalinitialvelocity = ((horizontalfinalvelocity ** 2) - (2 * horizontalacceleration * horizontaldisplacement)) ** 0.5
                initialvelocity = horizontalinitialvelocity / math.cos(projectionangle)
            elif Hashorizontaldisplacement != 'yes': #no horizontal displacement value, so uses suvat equation which doesn't involve horizontal displacement.
                horizontalinitialvelocity = (horizontalfinalvelocity - (horizontalacceleration * totaltime))
                initialvelocity = horizontalinitialvelocity / math.cos(projectionangle)
            elif Hashorizontalfinalvelocity != 'yes': #no horizontal final velocity value, so uses suvat equation which doesn't involve horizontal final velocity.
                horizontalinitialvelocity = (horizontaldisplacement - (0.5 * horizontalacceleration * (totaltime ** 2))) / totaltime
                initialvelocity = horizontalinitialvelocity / math.cos(projectionangle)
            else: #must not have horizontal acceleration value, so uses suvat equation not involving horizontal acceleration.
                horizontalinitialvelocity = (2 * horizontaldisplacement / totaltime) - horizontalfinalvelocity
                initialvelocity = horizontalinitialvelocity / math.cos(projectionangle)
        elif Verticalcounter > 2: #code uses same logic as above, but repeated for vertical motion.
            if Hastotaltime != 'yes':#no time value, so uses suvat equation which doesn't involve time.
                verticalinitialvelocity = ((verticalfinalvelocity ** 2) - (2 * verticalacceleration * verticaldisplacement)) ** 0.5
                initialvelocity = verticalinitialvelocity / math.sin(projectionangle)
            elif Hasverticaldisplacement != 'yes': #no vertical displacement value, so uses suvat equation which doesn't involve vertical displacement.
                verticalinitialvelocity = (verticalfinalvelocity - (verticalacceleration * totaltime))
                initialvelocity = verticalinitialvelocity / math.sin(projectionangle)
            elif Hasverticalfinalvelocity != 'yes':#no vertical final velocity value, so uses suvat equation which doesn't involve vertical final velocity.
                verticalinitialvelocity = (verticaldisplacement - (0.5 * verticalacceleration * (totaltime ** 2))) / totaltime
                initialvelocity = verticalinitialvelocity / math.sin(projectionangle)
            else:#must not have vertical acceleration value, so uses suvat equation not involving vertical acceleration.
                verticalinitialvelocity = (2 * verticaldisplacement / totaltime) - verticalfinalvelocity
                initialvelocity = verticalinitialvelocity / math.sin(projectionangle)
    else: #this is if no angle of projection provided, so both initial horizontal and vertical velocities must be calculated for pythagoras theorem.
        if Horizontalcounter <= 1 and Verticalcounter <= 1: #if less than 2 values of horizontal or vertical motion for both provided, impossible to calculate initial velocity.
             print("Not enough information provided")
             exit()
        if (Horizontalcounter == Verticalcounter and Horizontalcounter > 2) or (Horizontalcounter > 3 and Verticalcounter > 3):#code if both horizontal and vertical values are the same and above 2, or if both values are above 3.
            if Hastotaltime != 'yes': #suvat equation with no time value.
                horizontalinitialvelocity = ((horizontalfinalvelocity ** 2) - (2 * horizontalacceleration * horizontaldisplacement)) ** 0.5
                verticalinitialvelocity = ((verticalfinalvelocity ** 2) - (2 * verticalacceleration * verticaldisplacement)) ** 0.5
            elif Hashorizontaldisplacement != 'yes': #suvat calculation with no horizontal displacement value.
                horizontalinitialvelocity = (horizontalfinalvelocity - (horizontalacceleration * totaltime))
            elif Hashorizontalfinalvelocity != 'yes': #suvat calculation with no horizontal final velocity value.
                horizontalinitialvelocity = (horizontaldisplacement - (0.5 * horizontalacceleration * (totaltime ** 2))) / totaltime
            else: #suvat equation with no horizontal acceleration value.
                horizontalinitialvelocity = (2 * horizontaldisplacement / totaltime) - horizontalfinalvelocity
            if Hasverticaldisplacement != 'yes': #suvat equation with no vertical displacement value.
                verticalinitialvelocity = (verticalfinalvelocity - (verticalacceleration * totaltime))
            elif Hasverticalfinalvelocity != 'yes': #suvat equation with no vertical final velocity value.
                verticalinitialvelocity = (verticaldisplacement - (0.5 * verticalacceleration * (totaltime ** 2))) / totaltime
            else: #suvat equation with no vertical acceleration value.
                verticalinitialvelocity = (2 * verticaldisplacement / totaltime) - verticalfinalvelocity
            initialvelocity = (horizontalinitialvelocity ** 2 + verticalinitialvelocity ** 2) ** 0.5 #pythagoras theorem to calculate initial velocity.
        elif Horizontalcounter == 3 and Verticalcounter == 2: #requires calculation of horizontal initial velocity and time, and then uses time to calculate vertical initial velocity.
            if Hastotaltime != 'yes':
                horizontalinitialvelocity = ((horizontalfinalvelocity ** 2) - (2 * horizontalacceleration * horizontaldisplacement)) ** 0.5 #suvat to find horizontal initial velocity
                totaltime = (horizontalfinalvelocity - horizontalinitialvelocity) / horizontalacceleration #suvat equation using horizontal values to find time.
                if Hasverticaldisplacement != 'yes': #suvat equation to find vertical initial velocity with no vertical displacement.
                     verticalinitialvelocity = (verticalfinalvelocity - (verticalacceleration * totaltime))
                elif Hasverticalfinalvelocity != 'yes':#suvat equation to find vertical initial velocity with no vertical final velocity.
                     verticalinitialvelocity = (verticaldisplacement - (0.5 * verticalacceleration * (totaltime ** 2))) / totaltime
                else: #suvat equation to find vertical initial velocity with no vertical acceleration.
                     verticalinitialvelocity = (2 * verticaldisplacement / totaltime) - verticalfinalvelocity
                initialvelocity = (horizontalinitialvelocity ** 2 + verticalinitialvelocity ** 2) ** 0.5 #calculating initial velocity using pythagoras theorem.
            else: #if only 2 values for either horizontal or vertical motion provided, with one of them already being time, it is impossible to then find initial vertical AND horizontal velocity.
                print("Not enough information provided")
                exit()
        elif Horizontalcounter == 2 and Verticalcounter == 3: #requires calculation of vertical initial velocity and time, and then uses time to calculate horizontal initial velocity.
            if Hastotaltime != 'yes':
                verticalinitialvelocity = ((verticalfinalvelocity ** 2) - (2 * verticalacceleration * verticaldisplacement)) ** 0.5 #suvat to find verticalinitial velocity
                totaltime = (verticalfinalvelocity - verticalinitialvelocity) / verticalacceleration #suvat equation using verticalvalues to find time.
                if Hashorizontaldisplacement != 'yes': #suvat equation to find horizontal initial velocity with no horizontal displacement.
                     horizontalinitialvelocity = (horizontalfinalvelocity - (horizontalacceleration * totaltime))
                elif Hashorizontalfinalvelocity != 'yes': #suvat equation to find horizontal initial velocity with no horizontal final velocity.
                     horizontalinitialvelocity = (horizontaldisplacement - (0.5 * horizontalacceleration * (totaltime ** 2))) / totaltime
                else: #suvat equation to find horizontal initial velocity with no horizontal acceleration.
                     horizontalinitialvelocity = (2 * horizontaldisplacement / totaltime) - horizontalfinalvelocity
                initialvelocity = (horizontalinitialvelocity ** 2 + verticalinitialvelocity ** 2) ** 0.5 #calculating initial velocity using pythagoras theorem.
            else: #if only 2 values for either horizontal or vertical motion provided, with one of them already being time, it is impossible to then find initial vertical AND horizontal velocity.
                print("Not enough information provided") #any other combination of horizontal and vertical values mean it is impossible to calculate initial velocity.
                exit()
        else:
            print("Not enough information provided")
            exit()
    print(initialvelocity) #prints value of initial velocity to user.
    return initialvelocity #returns value of initial velocity to main code.
            
def calculatetotaltime(): #define function to calculate total time taken for motion
    global horizontalinitialvelocity #ensures all variables with command have same value both inside and outside of this function
    global horizontalfinalvelocity
    global horizontaldisplacement
    global horizontalacceleration
    global totaltime
    global verticalinitialvelocity
    global verticalfinalvelocity
    global verticaldisplacement
    global verticalacceleration

    if Horizontalcounter < 3 and Verticalcounter < 3: #if less than 3 values of horizontal or vertical motion given, impossible to calculate total time taken
        print("Not enough information provided")
        exit()
    if Horizontalcounter > 2:
        if Hashorizontalinitialvelocity != 'yes': #uses suvat equation to calculate horizontal initial velocity, which is then used to calculate total time.
            horizontalinitialvelocity = ((horizontalfinalvelocity ** 2) - (2 * horizontalacceleration * horizontaldisplacement)) ** 0.5
            totaltime = (horizontalfinalvelocity - horizontalinitialvelocity) / horizontalacceleration
        elif Hashorizontaldisplacement != 'yes': #no horizontal displacement value, so uses suvat equation which doesn't involve horizontal displacement.
            totaltime = (horizontalfinalvelocity - horizontalinitialvelocity) / horizontalacceleration
        elif Hashorizontalfinalvelocity != 'yes': #uses suvat equation to calculate final velocity, which is then used to calculate total time.
            horizontalfinalvelocity = ((horizontalinitialvelocity ** 2) + (2 * horizontalacceleration * horizontaldisplacement)) ** 0.5
            totaltime = (horizontalfinalvelocity - horizontalinitialvelocity) / horizontalacceleration
        else: #must not have horizontal acceleration value, so uses suvat equation not involving horizontal acceleration.
            totaltime = ((2 * horizontaldisplacement) / (horizontalinitialvelocity + horizontalfinalvelocity))
    elif Verticalcounter > 2: #code uses same logic as above, but repeated for vertical motion.
        if Hasverticalinitialvelocity != 'yes': #uses suvat equation to calculate vertical initial velocity, which is then used to calculate total time.
            verticalinitialvelocity = ((verticalfinalvelocity ** 2) - (2 * verticalacceleration * verticaldisplacement)) ** 0.5
            totaltime = (verticalfinalvelocity - verticalinitialvelocity) / verticalacceleration
        elif Hasverticaldisplacement != 'yes': #no vertical displacement value, so uses suvat equation which doesn't involve vertical displacement.
            totaltime = (verticalfinalvelocity - verticalinitialvelocity) / verticalacceleration
        elif Hasverticalfinalvelocity != 'yes': #uses suvat equation to calculate final velocity, which is then used to calculate total time.
            verticalfinalvelocity = ((verticalinitialvelocity ** 2) + (2 * verticalacceleration * verticaldisplacement))
            totaltime = (verticalfinalvelocity - verticalinitialvelocity) / verticalacceleration
        else: #must not have vertical acceleration value, so uses suvat equation not involving vertical acceleration.
            totaltime = ((2 * verticaldisplacement) / (verticalinitialvelocity + verticalfinalvelocity))
    else:
        print("Not enough information provided")
        exit()
    print(totaltime) #prints value of total time taken to user.
    return totaltime #returns value of total time taken to main code.


#ask user what value they want to calculate

Variabletocalculate = str(input("What value would you like to calculate?"))
Variabletocalculate = Variabletocalculate.lower() #convert input to lowercase so easy to compare

#check which value the user inputted 
if Variabletocalculate == "initial velocity":
    initialvelocity = calculateinitialvelocity()
#elif Variabletocalculate == "final velocity":
    
elif Variabletocalculate == "time taken":
    totaltime = calculatetotaltime()
#if Variabletocalculate == "total distance travelled":
    
#if Variabletocalculate == "tallest height reached":


