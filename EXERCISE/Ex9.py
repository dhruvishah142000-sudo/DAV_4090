# Check Age and find you are child , tinager , adult or senior citizen.

age = int(input("Enter Age : "))

if age>=1 and age<=12:
    print(f"your age is {age} , You are Child.")

elif age>=13 and age<=19:
    print(f"your age is {age} , You are Tinager.")

elif age>=20 and age<=60:
    print(f"your age is {age} , You are Adult.")

else:
    print(f"your age is {age} , You are Senior Citizen.")

    
