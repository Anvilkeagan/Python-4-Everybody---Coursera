### Challenge
# open file "romeo.txt
# read line by linefor each line
    # split line into list of wortds using split method
# build list of words
    # for each word on each line check to see if the word is in the list and if not append
# after list is created sort alphabetical
# print

#prompt user for a file to analyse
fname = input("Enter file name: ")

#open handle and initialize list variable
fh = open(fname)
lst = list()

#loop though each line and split into constituent words and save to a temp list
for line in fh:
    splitline=line.split()
    
    #Loop through temp list of words to analyse each word individually
    for word in splitline:
        
        #if the word is already in the list skip that word - else append to the list
        if word in lst:
            continue
        else:
            lst.append(word)

#sort and print            
lst.sort()
print(lst)