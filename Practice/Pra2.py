# WAP to create Fibonacci series upto entered terms.

val = int(input("Enter a value : "))

print("Fibonaci Series : ")

n1 = 0
n2 = 1
print(n1,n2,sep="\n")

for i in range(2,val+1):
    t = n1+n2
    print(t)

    n1 = n2
    n2 = t


