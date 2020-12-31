'''Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .'''


N=input()
i=0

if int(N)>=1 and int(N)<=20:
    for i in range(int(N)):
        print(i**2)
        i+=1
else:
    print("Constraint Broke")
