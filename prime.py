#prime
number=int(input("enter your number:"))
for i in range(2,number):
    if number%i==0:
        print("not prime:",number)
else:
    print("prime:",number)
