#defining a function that calculates pay including a consideration for overtime
def computepay(h,r):
    if h<40:
        pay=h*r
        return pay   
    else:
        pay=(h-40)*r*1.5+40*r
        return pay

#prompt for user input
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    #convert type 
    hrsf=float(hrs)
    ratef=float(rate)
    
    #call defined function
    p = computepay(hrsf,ratef)
    print("Pay",p)

except:
    print("Please enter numeric values")