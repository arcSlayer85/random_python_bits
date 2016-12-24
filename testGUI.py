from tkinter import *;

def getEntry():
    ent = inp_bo.get();
    print(ent);
    outputBox.insert(END, ent);

main = Tk();
main.geometry('300x300');
main.title('This is a test...');

nameLab = Label(main, text = 'Name : ');
nameLab.grid(row = 1, column = 1);

inp_bo = Entry(main);
inp_bo.grid(row = 1, column = 2);

oplab = Label(main, text = 'Output : ');
oplab.grid(row = 3, column = 1);

outputBox = Text(main, height = 1, width = 30);
outputBox.grid(row = 3, column = 2);

submit = Button(main, text = 'Submit', command = getEntry());
submit.grid(row = 2, column = 2);

main.mainloop();







        
