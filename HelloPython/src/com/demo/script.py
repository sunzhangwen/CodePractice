#code=utf8
'''
Created on Sep 29, 2016

@author: sunzhangwen
Change on Dec 02, 2016 i am back
'''
#code=utf8
import time
import src.com.demo.StringUtil
from src.com.demo import StringUtil

"""
Python get orientation
"""
print("Hello Python")

name = "Bruce"
print("Nice to see you %s, good morning!" %name)

age = 27
print("You are %d." %age)
print("Hi %s, I know your %d" %(name,age))

# When you don't know whick type it is
pi = 3.1415926
print("Pi is %r" %pi)
name = 'Wayne'
print("Hello %r" %name)

# input data throught key board
# n = input("Enter what you want:")
# print("You enter %r, is that right?" %n)

# import Model
print(time.ctime())
print("测试程序")
time.sleep(1)
print(time.ctime())

print(StringUtil.add(60, 90))



