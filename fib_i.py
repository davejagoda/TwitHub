#!/usr/bin/python

def f(n):
 a=0;b=1
 for i in range(n): a,b=b,a+b
 return a

import sys
print f(int(sys.argv[1]))
