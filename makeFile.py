#! /usr/bin/python

import os, time

_input = input("Make a folder?")

if _input == "yes" or _input =="y":
    filename_ = input("Name it..")
    os.makedirs('C:\\Users\\djs85\\Desktop\\' + filename_);
elif _input == "no" or _input == "No":
    print("GoodBye");
    time.sleep(2);


      
