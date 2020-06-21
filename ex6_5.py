##Strip the last number from the text, convert to float and print

#text to analyse
text = "X-DSPAM-Confidence:    0.8475";

#finding the start of the number
#I know this isn't a great way of doing this
pos=text.find('0')

#slicing
numstr=text[pos:]

#type conversion
num=float(numstr)
print(num)