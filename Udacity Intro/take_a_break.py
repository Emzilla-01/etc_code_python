# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import webbrowser
import time
import os

break_interval = 120
iters = 0
while iters <= 2:
    time.sleep(break_interval)
    webbrowser.open('https://www.youtube.com/watch?v=EUvmCuPjHD4')
    iters += 1
print("All done!")
os.listdir(r'C:\Users\orpha\AppData\Local\conda\conda\envs\py27')

# =============================================================================
# 
# =============================================================================

os.chdir(r'C:\EnvVariables')
os.listdir(os.getcwd())

os.rename('bleep.txt', 'bloop.txt')
os.rename('test1.txt', 'test2.txt')
