"""
Automate the Boring Stuff with Python: Organizing Files...

"""

import shutil, os;

# os.listdir(path), lists the folders in the 'path' directory, below we print
# the name of every folder in the 'test' folder...

path = 'C:\\Users\\djs85\\Desktop\\test';
path_dirs = os.listdir(path);
for file in path_dirs:
    print(file);

# copy a file (source, destination), in this case copying the text file text.txt
# from it's folder location to the desktop...

shutil.copy('C:\\Users\\djs85\\Desktop\\test\\test1\\text.txt', 'C:\\Users\\djs85\\Desktop\\');

# copy a folder and it's contents and file path(folder path, copied folder path)
# the following makes a copy of the folder 'test' on the Desktop called 'test_backup'...

shutil.copytree('C:\\Users\\djs85\\Desktop\\test', 'C:\\Users\\djs85\\Desktop\\test_backup');

# moving a file or folder path (source, destination), below we move the folder 'test_backup',
# which we created above, into the 'test' folder, then back onto the 'Desktop'...

shutil.move('C:\\Users\\djs85\\Desktop\\test_backup', 'C:\\Users\\djs85\\Desktop\\test');

shutil.move('C:\\Users\\djs85\\Desktop\\test\\test_backup', 'C:\\Users\\djs85\\Desktop\\');

# delete a single file or single empty folder using the os module, otherwise
# deleting a folder and all of it's contents requires the shutil module...

# os.unlink(path) will delete file at 'path'...
# os.rmdir(path) will delete the folder at 'path', folder must be empty...
# shutil.rmtree(path) will remove the folder at path and all files and folders contained within...

path = 'C:\\Users\\djs85\\Desktop\\test_backup';
shutil.rmtree(path);

text_file = 'C:\\Users\\djs85\\Desktop\\text.txt';
os.unlink(text_file);

path = 'C:\\Users\\djs85\\Desktop\\test';
path_dirs = os.listdir(path);
for file in path_dirs:
    print(file);










