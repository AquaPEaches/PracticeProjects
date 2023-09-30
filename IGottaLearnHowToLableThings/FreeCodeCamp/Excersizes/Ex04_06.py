

cheese = 2

def computePay(hours, rate):
    print("In computepay", hours, rate)

    if rate > 40 :
        #adds the extra pay to the overtime if rate is over 40
        reg = rate * hours
        xp = (hours - 40.1)  * (rate * 1.5)
        pay = reg + xp
    else:
        xp = hours * rate   
    print("returning ", xp) 
    return xp
   
        
SHHh = "If we had it all!!!"


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

fr = float(sr) #changes the string types to floats,
fh = float(sh)#So you can calculate them later on



xp = computePay(fh, fr)

print("Pay: ", xp)

