import hashlib
import re

try:
    p = re.compile('\d{8}')
    log=0
    f=0
    flag=0
    start_num=10000000
    rewrite="w"
    try:
        with open("hash500\\save", "r") as fl:
            save=fl.read()
            m=p.match(save)
            if(m):
                start_num=int(m.group())
                rewrite="a"
                print("hash500\\"+str(start_num-(start_num%5000000))+".txt")
                f=open("hash500\\"+str(start_num-(start_num%5000000))+".txt",rewrite)
                flag=1
    except Exception as e:
        raise e

    for i in range(start_num,100000000):
        if(i%5000000==0):
            if(flag==1):
                f.close()
            f=open("hash500\\"+str(i)+".txt",rewrite)
            flag=1
        temp=str(i)+"salt_for_you"
        for j in range(0,500):
            h=hashlib.sha1()
            h.update(temp.encode('utf-8'))
            temp=h.hexdigest()
        f.write(str(i)+"\t"+temp+"\n")
        with open("hash500\\save", "w") as fl:
            fl.write(str(i))
        if(log==0):
            log=str(i)+"\t"+temp+"\n"
            print(log)
        log=str(i)+"\t"+temp+"\n"
except KeyboardInterrupt:
        print('Interrupted')
        with open("hash500\\save", "w") as fl:
            fl.write(str(log))
    
