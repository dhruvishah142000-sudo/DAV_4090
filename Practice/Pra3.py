# WAP TO CHECK GIVEN NUMBER IS ARMSTRONG NUMBER OR NOT

num = int(input("enter a number : "))

t = num

sum = 0

digit = len(str(t))

while t>0:
    digits = t%10
    sum += digits ** digit
    t//=10

if sum==num:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")
