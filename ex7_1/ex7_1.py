###challenge###
#prompt for file name
#open file
#reads file
#print contents in uppercase
#file=works.txt

# Use words.txt as the file name
fname = input("Enter file name: ")

#try to open a socket to the file listed about, quit on failure with message
try:
    fhandle=open(fname,'r') 
    
except:
    print("Couldnt open handle")
    quit()

# read into a variable and apply upper method before printing    
temp=fhandle.read()
tempUpper=temp.upper()
print(tempUpper)