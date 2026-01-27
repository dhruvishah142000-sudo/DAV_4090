# Num is pos.,neg.,zero...

try:
    
    n1 = int(input("Enter Number : "))

    if n1>=1:
        print(f"{n1} is Positive Number.")

    elif n1<0:
        print(f"{n1} is Negative Number.")

    else:
        print(f"Number is {n1}.")

except ValueError:
    print("Wrong Input...")


