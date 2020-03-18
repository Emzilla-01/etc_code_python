# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:50:12 2019

@author: emmam
"""

def reversed_args(*args):
    if len(args)==1:
        return(None)
    i=0
    l=[]
    for a in args:
        if i==0:
            f = a
            print(f)
            print(type(f))
            if type(f) in [type(pow)]:
                f = a.__name__
            else:
                return(Exception("First arg must be func"))
        else:
            l.append(a)
        i+=1
    l.reverse()
    l=str(l)
    l= l.replace("[", "")
    l= l.replace("]", "")
    print(l)
    r=f"{f}({l})"
    return(eval(r))
     
#pow(3,3)
reversed_args(pow,2,3)
reversed_args

from inspect import signature, getcallargs

list(getcallargs(pow, 2, 3, z=0).items())


from functools import partial

def reversed_args(f):
    f = partial(f, args=list(getcallargs(f).items())[::-1])
    return(f)
    
reversed_args(pow)

from collections import defaultdict


dd = defaultdict(int)
dd[1]
dd[1]+=1


def sockMerchant(n, ar):
    get_pairs = lambda n: n//2 if (n//2 > 0) else 0
    pairs=[]
    dd = defaultdict(int)
    for i in ar:
        dd[i]+=1
    for key in dd.keys():
        pairs.append(get_pairs(dd[key]))
    return(sum(pairs))
    
sockMerchant(7, [1,2,1,2,1,3,2])

       
            
                        
[1, 0, -1, -2, -1, -2, -1, 0]
a_d = {"U":+1, "D":-1}
is_negative = lambda i: (i!=0) and (abs(i)+i<1)

def countingValleys(n, s):
    s=list(s)
    s = [a_d.get(c) for c in s]
    #alt_a = [sum(s[:i+1]) for i in range(len(s))]
    #assert all([type(i) == int for i in arr])
    alt = 0
    vals = 0
    in_val = 0
    for i in s:
        alt+=i
        if is_negative(alt):
            in_val = 1
        if in_val and not is_negative(alt):
            in_val = 0
            vals+=1
    return(vals)
    
    return(s, alt_a)
countingValleys(8, "UDDDUDUU")

def jumpingOnClouds(c):
    steps=0
    ei=0
    while ei+2 < len(c):
#        print(f"ei:{ei}, steps:{steps}")
        if c[ei+2] == 0:
            ei+=2
            steps+=1
            continue
        if c[ei+2] == 1:
            ei+=1
            steps+=1
            continue
    while ei+1 < len(c):       
        if c[ei+1] == 1:
            ei+=2
            steps+=1
            continue        
        if c[ei+1] == 0:
            ei+=1
            steps+=1
            continue
    if ei+1 == len(c):
        return(steps)
    return(steps)
    
jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
