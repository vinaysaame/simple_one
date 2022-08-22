#write a function of fabonacci series
def fabinocci(x):
    n1=0
    n2=1
    for i in range(x):
        n3=n1+n2
        print(n1)
        n1=n2
        n2=n3

print(fabinocci(10))
