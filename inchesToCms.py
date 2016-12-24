#! /usr/bin/python

"""
program that offers the user the choice of converting cm to inches or
inches to centimetres. Use functions for each of the conversion programs.
"""

# Function for cm's to inches...
def calculateCms ( int ):

    _cm = _height * 2.54;

    print (_cm);

# function for inches to cm's...
def calculateInches ( int ):

    _inches = _height / 2.54;

    print (_inches);

# get the type of conversion the user wants to do...
convType = int(input("Your height inches/centimeters(1) \nor centimeters/inches(2)?..."));


# If they press 1, do this...
if convType == 1:
    _height = int(input("Enter your height in inches..."));
    calculateCms(_height);
    
# If they press 2, do this...
else:
    if convType == 2:
        _height = int(input("Enter your height in centimeters..."));
        calculateInches(_height);
