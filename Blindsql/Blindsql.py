import requests
import threading
import re
from lxml.html import fromstring, tostring

class Thread1(threading.Thread):
    method=None
    target=None
    header=None
    body=None
    payload=None
    
    check=None
    source=None
    true=None
    keyword=None
    response=None
    
    def __init__(self,method,target,header,body,check):
        threading.Thread.__init__(self)
        self.method=method
        self.target=target
        self.header=header
        self.body=body
        
        self.check=check
        self.source=source
        self.true=true
        self.keyword=keyword

        

    def responseCheck(self,res,source,true,keyword):
        if check[0]==body:
            doc=fromstring(res.content)
            values=doc.xpath(source)
            if values==keyword:
                return True
            else:
                return False

    def run(self):
        if self.method=="GET":
            self.response=requests.get(self.target,params=self.body,headers=self.header)
            self.responseCheck(self.response,check)
            
        print("%s said : Thread %s die(time:%s)\n"%(self.file,self.ident,str(datetime.datetime.now())))


    def start(self):
        threading.Thread.start(self)
        return self._return

def checkTarget(method,host,url,header,body):
    if method=="GET":
        requests.get(host+url)
    if method=="POST":
        requests.post(host+url,data=body)

def payloadAssemble(source,payload,body):
    body[source]=body[source]+payload
    return body
    

def blindLoop(method,host,url,header,body):
    threading.Barrier(93, timeout=10)
    for i in range(33,126):
        globals()[i] = Thread1(
    if method=="GET":
        requests.get(host+URL,params=body)
        

def main(files):
    try:
        method=input("METHOD : \n")
        url=input("URL PATH : \n")
        host=input("HOST(protocol://host) : \n")
        headerline=input("HEADER(세션 또는 그외 접근 용)(몇개인지작성) : \n")
        header = [sys.stdin.readline().strip() for i in range(headerline)]
        body=input("BODY(parameter,json(?제외)) : \n")
        p=re.compile('&?(([^&=]*)(\=([^&]*))?)&?')
        m=p.findall(body)
        body={x[1]:x[3] for x in m if x[0] != ''}
        source=input("SQL 취약부분(method,url,parameter,header,body) : \n")
        payload=input("SQL Payload : \n")

        checkTarget(method,host,url,body,header)
        for file in files:
            if not (p.match(file)):
                continue
            globals()[file] = Thread1("hash500\\"+file,search)
            globals()[file].start()
        #j2.start()

        #j2.join()
        """if off == 1:
            j1.flag.set()
            j1.join()"""
    except Exception as e:
        print(e)

if __name__ == '__main__':
    onlyfiles = [f for f in listdir("hash500") if isfile(join("hash500", f))]
    main(onlyfiles)
    
