"""
Write a program that reads a value from the user in cm and calculates the number
of inches.
The equation to use is:

centimeters = inches * 2.54
"""

# This is a function, an integer (int(height)) is being passed to it...
def calculateHeight ( int ):

    _inches = height / 2.54;

    print (_inches);

# Here is where it asks for the height integer to be entered...
height = int(input("Enter your height in centimeters...."));

# Here it passing the integer "height" into the function calculateHeight...
calculateHeight(height);

