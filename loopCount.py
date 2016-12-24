"""
Use count variable to use a loop as many times as you like...
"""

import time;
import datetime;
import random;

_datetime = datetime.datetime.now();

print (_datetime);

time.sleep(1);

print ("Hello, World!");
time.sleep(1);

count = 0;

def randomNumber():
	global count;
	while count != 5:
		_randomNumber = random.randint(1,100);
		print (_randomNumber);
		count = count + 1;
		time.sleep(1);

randomNumber();

print (count);

