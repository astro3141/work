import sys
import threading

b=threading.Barrier(1,timeout=10)

b.wait()
n = 1
data = [sys.stdin.readline().strip() for i in range(n)]
