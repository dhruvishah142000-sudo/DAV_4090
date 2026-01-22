# Result

per = int(input("Enter Percentage : "))

if per>=90:
    print("Grade - Distinction")

elif per>=70 and per<=90:
    print("Grade - First Class")

elif per>=60 and per<=69:
    print("Grade - Second Class")

elif per>=50 and per<=59:
    print("Grade - Third Class")

else:
    print("Grade - Fail")
