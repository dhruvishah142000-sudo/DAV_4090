''' WAP to enter the their working hour to calculate gross pay and the pro.should give emp.
1.5 times if working hour is above 30 hours.'''

h = float(input("Enter Hour : "))
r = float(input("Enter Rate Per Hour : "))

if h>=30:
    final = (h*r)+((h-30)*r*1.5)

else:
    final = (h*r)

print("Your final gross pay is : ",final)
