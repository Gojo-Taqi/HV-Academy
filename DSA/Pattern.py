n=int(input("Enter the value of n:"))
num=1
for i in range(0,int((n+1)/2)):
    for j in range(0,n):
        print(num,end=" ")
        num=num+1
    print()
    num=num+n
n1=int(n/2)
for i in range(0,int(n/2)):
    Num=n*2*n1
    for j in range(1,n+1):
        print(Num-(n-j), end=" ")
    print()
    n1=n1-1