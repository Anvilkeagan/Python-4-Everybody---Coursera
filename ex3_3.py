#Prompt the user for an input
score_str=input("Enter Score: ")

#exception handling for unexpected data type
try:
    score=float(score_str)
    
    #exception handling for input out of range
    if score>1:
        print("Please provide a score between 0-1")
    elif score<0:
        print("Please provide a score between 0-1")
        
    #Printing Scores    
    else:
        if score<0.6:
            print("F")
        elif score<0.7:
            print("D")
        elif score<0.8:
            print("C")        
        elif score<0.9:
            print("B")
        else:
            print("A")
            
except:
    print("Please provide a numeric score")