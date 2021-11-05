import hashlib
import re

p = re.compile('\d{8}')
log=0
f=0
flag=0
start_num=10000000
rewrite="w"
try:
    with open("D:\\work\\webhacking\\hash500\\save", "r") as fl:
        save=fl.read()
        m=p.match(save)
        if(m):
            start_num=save
            rewrite="a"
except Exception as e:
    pass

for i in range(start_num,100000000):
    if(i%5000000==0):
        if(flag==1):
            f.close()
        f=open("D:\\work\\webhacking\\hash500\\"+str(i)+".txt",rewrite)
        flag=1
    temp=str(i)+"salt_for_you"
    for j in range(0,500):
        h=hashlib.sha1()
        h.update(temp)
        temp=h.hexdigest()
    f.write(str(i)+"\t"+temp+"\n")
    with open("D:\\work\\webhacking\\hash500\\save", "w") as fl:
        fl.write(str(i))
    if(log==0):
        log=str(i)+"\t"+temp+"\n"
        print(log)
    
