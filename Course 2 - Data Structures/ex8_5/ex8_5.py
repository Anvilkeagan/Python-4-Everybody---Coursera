### Challenge
# open file "mbox-short.txt"
# read line by line
    # for lines starting with from
    # split line into list of wortds using split method
    # Print second word 
    # count lines
# print print count


#prompt for file name with default file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

#open sockets and intialize 
fh = open(fname)
count = 0

#loop through each line
for line in fh:

    #I still dont understand why we do this rstrip
    line=line.rstrip()
    
    #ignore lines not starting with 'From'
    if not line.startswith('From'):
        continue

    #split line into words
    words=line.split()
    
    # exploration of the data showed that each message contained multiple lines
    # starting with from
    # Although the challenge implicitly specify we only want the first 'from' per email
    # initially I interpreted this incorrectly
    # in total there are 54 lines starting with from
    # 11 unique
    # but 27 messages
    # the lines we want follow thje format "From address dd M D HH:MM:SS YYYY" so I just check for the length
    if len(words)>3:
        print(words[1])
        count=count+1
        
print("There were", count, "lines in the file with From as the first word")