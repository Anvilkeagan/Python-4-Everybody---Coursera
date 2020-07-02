## Challenge
# Write a program to read through the mbox-short.txt
# distribution by hour of the day (strip and count?)
# each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time
 # and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1



#prompt for file name with default file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

#open sockets and intialize 
fh = open(fname)
counts=dict()

#loop through each line
for line in fh:

    #I still dont understand why we do this rstrip
    line=line.rstrip()
    
    #ignore lines not starting with 'From'
    if not line.startswith('From'):
        continue

    #split line into words
    words=line.split()
    
    # filter for the right line starting with from (more than 3 elements)
    if len(words)>3:
    
        # slice time then hour out
        time=words[5]
        hour=str(time[:2])
        
        # use get method to put together a distribution in the form of a dictionary
        counts[hour]=counts.get(hour,0)+1
    
# sort the list by keys
sortedcount=sorted(counts.items())

# loop through dictionary and print key,value   
for hour,count in sortedcount:

    # print results 
    print(hour,count)


