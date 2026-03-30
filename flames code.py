b=input("enter a name:")
g=input("enter a name:")
num=len(b)+len(g)
for i in range(len(b)):
    for j in range(len(g)):
        if b[i]==g[j]:
            num=num-2
            g.replace("j","?")
            break
tot=num
if tot==1:
    print("sister")
if tot==2 or tot==4 or tot==7 or tot ==9:
    print("enemy")
if tot==6:
    print("Marriage")
if tot==8:
    print("Affection")
if tot==10:
    print("Love")
if tot==5 or tot==3:
    print("Friend")