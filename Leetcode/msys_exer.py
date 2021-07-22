#problem 1:
#valid ip

def check_range(ipv4):
    counter=0
    for i in ipv4:
        if 0<=int(i)<=255:
            counter+=1
    if counter==4:
        return True
    else:
        return False
        


ip="174.122.2.22"

ipv4=ip.split(".")


if len(ipv4)==4 and check_range(ipv4):
    print("valid")
else:
    print("invalid")


#problem 2
#1*YY, 5*E, 2*RR


inpt="1*YY, 5*E, 2*RR"
res=inpt.split(",")
#print(res)

l=[]
for i in res:
    i=i.strip()
    num=int(i[0])
    strng=i[2:]
    mul=str(strng)*(num)
    l.append(mul)

sl=" ".join(l)
print(sl)
    

#problem 3:
#occurance of words

s=" I am doing good, are you doing good too?"

ls=s.split()
print(ls)

d={}
for i in ls:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

print(d)
    
