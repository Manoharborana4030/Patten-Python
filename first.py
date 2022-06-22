n=5
for i in range(n+1):
    for j in range(i):
        print("*",end='')
    print("\r")

for i in range(n,0,-1):
    for j in range(i-1):
        print("*",end='')
    print("\r")
temp=0
for i in range(n+1):
    for sp in range(n,i,-1):
        print(end=" ")
    for j in range(i*2):
        if temp==0:
            temp+=1
            pass
        else:
            print("*",end='')
    print("\r")

ran=1
for i in range(n,0,-1):
    for sp in range(ran):
        print(end=' ')
    for j in range((i-1)*2):
        print("*",end='')
    
    print("\r")
    ran+=1








