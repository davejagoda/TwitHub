#!/usr/bin/python

def f(n):
 if n<2: return n
 return f(n-1)+f(n-2)

import sys
print f(int(sys.argv[1]))
