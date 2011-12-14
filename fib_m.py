#!/usr/bin/python

def f(n):
 if n<2: g[n]=n
 try: g[n]
 except: g[n]=f(n-1)+f(n-2)
 return g[n]

g={}
import sys
print f(int(sys.argv[1]))
