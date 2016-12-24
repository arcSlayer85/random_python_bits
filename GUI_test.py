# tkinter imports a framework for making a GUI/window app..

from tkinter import *;

top = Tk();

b1 = Button(top, text = 'Button 1');
b2 = Button(top, text = 'Button 2');
b3 = Button(top, text = 'Button 3');
b4 = Button(top, text = 'Button 4');

b1.pack(side = LEFT, padx = 10);
b2.pack(side = LEFT, padx = 10);
b3.pack(side = RIGHT, padx = 10);
b4.pack(side = RIGHT, padx = 10);

top.mainloop();

"""

from tkinter import *;

# create instance of Tk
main = Tk();

# name the window (str)
main.title('DJS');

# set the window icon
main.wm_iconbitmap('JAH.ico');

# window size
main.geometry('500x500');

# draw window, open application
main.mainloop();




