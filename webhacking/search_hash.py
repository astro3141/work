import threading
import time
from os import listdir
from os.path import isfile, join
import re
import datetime

off = 0
class Thread1(threading.Thread):
    file=None
    target=None
    _return=None
    def __init__(self,file,target):
        threading.Thread.__init__(self)
        self.flag = threading.Event()
        self.file=file
        self.target=target

    def run(self):
        print("%s said : Start\n"%(self.file))
        p=re.compile('(.*?)\t?([0-9a-f]{40}).*?')
        with open(self.file, "r") as fl:
            while not self.flag.is_set():
                line = fl.readline()
                if not line:
                    self._return=None
                    break
                m=p.match(line)
                search=m.group(2)
                if(search==self.target):
                    self._return=line
                    self.flag.set()
                    print(datetime.datetime.now())
                    break
        print("%s said : Thread %s die(time:%s)\n"%(self.file,self.ident,str(datetime.datetime.now())))


    def start(self):
        threading.Thread.start(self)
        return self._return


def main(files):
    try:
        search=input("해쉬값을 입력 : \n")
        p=re.compile('.*\.txt')
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
    
