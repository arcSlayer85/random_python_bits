# import the os module...
import os;

# list...
myFiles = ['file1.txt', 'file2.txt', 'file3.txt'];

# os.path.join will add the filenames in myFiles to the string file path...
for filename in myFiles:
    print(os.path.join('C:\\Users\\djs85\\Desktop', filename));

# store and print the absolute file path of a folder in a variable...
file = os.path.abspath('.\\test.txt');
print(file);

# store and print the size of the file...
size = os.path.getsize(file);
print(size);

# open the file in read mode ('r') and save it in a variable (openFile)...
openFile = open(file, 'r');

# read the contents of the file...
fileContent = openFile.read();

# close the file and re-open it in append mode ('a')...
openFile.close()
openFile = open(file, 'a')

# append the file with the given string, print the contents and then close it...
openFile.write('\nGoodbye, World!!!');

print(fileContent);

openFile.close();
