# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:17:50 2018

@author: orpha
"""
import datetime
handle = open('testfileMar1818.txt', 'wt', encoding = 'utf-8')
handle.write('Wolf came. %s '%(str(datetime.datetime.now())))
handle.close()

handle = open('testfileMar1818.txt', 'rt', encoding = 'utf-8')
handle.read()

dir(handle)
handle.closed # This is an attribute of a _io.TextIOWrapper object
type(handle) # 


"""
try/finally is better than try/except?
Multiple exceptions occur but still, the state of x is 'bar'.
"""
x = 'a state'
try:
    Exception
    name_error for syntax
    TypeError
finally:
    x = 'foo'
    x = 'bar'
x
