### Challenge
# Write a program to read through the mbox-short.txt
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines 
# takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.

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
    
# Using list slicing to add counts to dicts
    if len(words)>3:
        counts[words[1]]=counts.get(words[1],0) + 1


# intialize max loop variables 
maxcount=0
maxword=0

for word,count in counts.items():

# Guardian clause and word comparison
    if maxcount is None or count>maxcount:
        maxcount=count
        maxword=word

#print results 
print(maxword,maxcount)


