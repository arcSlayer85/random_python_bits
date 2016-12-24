#! /usr/bin/python

import random

def main():
	
	min = 1
	max = 6
	roll_again = "yes"
	
	while roll_again == "yes" or roll_again == "y":
		print ("Rolling the Dice...")
		print ("you rolled a...")
		print (random.randint(min, max))
		roll_again == input ("Roll again?...")

if roll_again == "no":
        
main()
