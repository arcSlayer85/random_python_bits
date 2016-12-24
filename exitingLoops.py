"""
A couple of ways to get out of loops
"""

import time;

# Although this is not a way out?...
def inputLoop():
	_input = "";
	while _input != "1" and _input != "2":
		_input = input("Enter a Number :");

# Use the count variable to break out of this...
def printStuff():
	global count;
	_input = str(input("Enter a Command :"));
	if _input == "This":
		if count == 0:
			print ("You are here");
			count = 1;



count = 0;

inputLoop();

printStuff();

time.sleep(2);

print ("count is at %i" % (count));

time.sleep(1);
