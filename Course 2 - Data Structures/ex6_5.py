##Strip the last number from the text, convert to float and print

#text to analyse
text = "X-DSPAM-Confidence:    0.8475";

#finding the start of the number
#I know this isn't a great way of doing this
## first version
#pos=text.find('0')

##second version
pos=text.find(':')

#slicing
numstr=text[pos+1:]

#type conversion
#stripping spaces
try:
    num=float(numstr.strip())
    print(num)
except:
    print("couldnt convert to float")