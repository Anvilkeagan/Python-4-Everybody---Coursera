### Challenge
# prompt for file name
# open and reads file
#looking for lines of the form: "X-DSPAM-Confidence:    0.8475"
# count these lines
# extract floating points
# compute average
# print Average spam confidence: 0.750718518519
# do not use sum
# Use the file name mbox-short.txt


# prompt for file name
try:
    fname = input("Enter file name: ")
    fh = open(fname,"r")
except:
    print("couldnt open file")
    quit()
    
#variable declaration
total=0
count=0

# loop through each line
for line in fh:
    #skip the unimportant lines
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    #pull the number 
    position=line.find(':')

    #slicing
    numstr=line[position+1:]

    #type conversion
    #stripping spaces
    try:
        num=float(numstr.strip())
    except:
        print("couldnt convert to float")
    
    # running count and total    
    count=count+1
    total=total+num

# average calculation    
avg=total/count

print("Average spam confidence: "+str(avg))



