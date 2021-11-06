
class Stackover4():

    header={}
    #headerSequence only input list [headername, type, length]
    headerSequence=[]
    payload=''

    flag={}
    flagSequence=[]
    
    @staticmethod
    def inttobit(integer, weight):
        
        if type(integer) is not int:
            raise Exception("inttobit's arg is only int")

        result = format(integer,'b')
        paddingLen = weight*8 - len(result)

        if paddingLen < 0:
            raise Exception("weight parameter is too large")
        elif paddingLen > 0:
            result = ('0'*paddingLen)+result
        else:
            pass
            
        return result


    @staticmethod
    def strtobit(string):
        
        if type(string) is not str:
            raise Exception("strtobit's arg is only String")
        
        result=[format(ord(i),'b') for i in string if len]
        
        for i in range(len(result)):
            if len(result[i]) != 8:
                result[i] = ('0'*(8-len(result[i])))+result[i]
                
        return ''.join(result)

        
    @staticmethod
    def bittobyte(bits):
        
        argType = type(bits)
        temp = [bits]
        resultBytes = bytearray()
        
        if len(bits)%8 != 0:
            padding = '0'*(8-(len(bits)%8))
        else:
            padding = ''
            
        if argType is list:
            for i in range(len(bits)):
                bits[i]=str(bits[i])
                if bits[i] != '0' and bits[i] !='1':
                    raise Exception("bittobyte's arg is only '0' or '1' data")
            bits.append(padding)
            bits = ''.join(bits)
        elif argType is str:
            temp.append(padding)
            bits = ''.join(temp)
        else:
            raise Exception("bittobyte's arg is only tuple, list or String")

        for i in range(len(bits)//8):
            eachByte = []
            integer = 0
            for j in range(8):
                eachByte.append(int(bits[(i*8)+j]))
            for k in range(8):
                integer = integer+(eachByte[k]<<(8-k-1))
            resultBytes.append(integer)
            
        return resultBytes


    def __init__(self):
        pass


    def setheaderSequenceOnce(self,**kwargs):
        pass


    def setheaderSequenceReculsive(self):
        name = input("type header name(if flag type flag)\n")
        types = input("type value't type(int,str,flg)\n")
        length = input("tpye header's length\n")
        if name != "":
            self.headerSequence.append([name,types,length])
            self.setheaderSequenceReculsive()

    def setHeader(self,name,value):
        if hasHeader:
            self.header[name] = value
        else:
            raise Exception("doesn't have header, you must regist header by setheaderSequenceOnce or setheaderSequenceReculsive")


    def setHeaderAuto(self):
        for i in self.headerSequence:
            value = input("input %s's value(type is %s and length is %d)\n"%(i[0],i[1],i[2]))
            self.setHeader(i[0],value)

    def setPayload(self):
        #abstrac after
        name = input("type query's name\n")
        types = input("type query's type\n")
        classes = input("type query's class\n")
        name = name.split(".")
        for i in name:
            if len(i)>63:
                raise Exception("query name is so long")
            self.inttobit(len(i),1)


    def setflagSequenceOnce(self):
        pass


    def setflagSequenceReculsive(self):
        name = input("type flag name\n")
        ranges = input("tpye flag's range(0 ~ n-1)\n")
        if name != "":
            self.flagSequence.append([name,ranges])
            self.setflagSequenceReculsive()


    def setFlag(self,name,value):
        ranges = checkFlag
        if ranges:
            self.flag[name] = value
        else:
            raise Exception("doesn't have flag or not match range, you must regist flag by setflagSequenceOnce or setflagSequenceReculsive")


    def setFlagAuto(self):
        for i in self.flagSequence:
            value = input("input %s's value(range is %s)\n"%(i[0],i[1]))
            self.setFlag(i[0],value)
                  

    def checkFlag(self,name):
        for i in self.flagSequence:
            if i[0] == name:
                return i[1]
            else:
                return False

    def hasFlag(self,name):
        for i in self.flagSequence:
            if i[0] == name:
                return True
        return False
    

    def checkHeader(self,name):
        for i in self.headerSequence:
            if i[0] == name:
                return i
        return False


    def hasHeader(self,name):
        for i in self.headerSequence:
            if i[0] == name:
                return True
        return False
        
            
dns = Stackover4()
dns.setheaderSequenceReculsive()
dns.setflagSequenceReculsive()

            
"""            
def bittobyte(bits):
    total = 0
    for i in range(len(bits)):
        if (bits[i] != 0 and bits[i] != 1):
            raise Exception("bittobyte's arg is only bit array")
        bits[i] = bits[i]<<(len(bits)-1)
        total = bits[i]+total
    total.to_bytes

payload=bytearray()

TranID=format(random.randrange(65535),b)
TranID=bytearray(TranId.to_bytes(2,byteorder='big')
flag=bytearray((4).to_bytes(2,byteorder='big')
Questions='1'
AnswerRRs='0'
AuthorityRRs='0'
AdditionalRRs='0'

Queries=''
Qtarget="www.spac.or.kr".split(".")
Qtarget.append('')
for q in Qtarget:
    Queries=Queries+str(len(q))+q
Type=1
Class=1
"""

"""
HOST='8.8.8.8'
PORT=53

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'')
    data = s.recv(1024)
print('Received',repr(data))
"""
