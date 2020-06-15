
#initialize values
max=None
min=None

while True:
    #prompt for user input
    numberstring = input("Enter an Integer:")
    
    #indefinite loop break on "done" input with printing results
    if numberstring=="done" :
        print("Maximum is", max)
        print("Minimum is", min) 
        break
    #None type cannot be compared to others - Need to set value manually 
    #to the intial value and convert to int for later type comparison
    if max is None:
        max=int(numberstring)
    if min is None:
        min=int(numberstring)
    try:    
        #convert type 
        numberint=int(numberstring)
        
        #comparing and storing the largest / smallest
        if numberint>max:
            max=numberint
        if numberint<min:
            min=numberint
   
    except:
        print("Invalid input")
        #continue