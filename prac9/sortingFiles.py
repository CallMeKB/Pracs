"""
CP1404 Prac 09 - From Scratch Exercise 
Program to sort through a directory, create subfolders for each extension type 
then move files to their correct subdirectory
"""
import os, shutil


def main():
    # show current directory
    print("Current directory is", os.getcwd())
    os.chdir('FilesToSort')
    # print(os.getcwd())
    extensions = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file = filename.split('.')
            # test print("file list is {}".format(file))
            if file[1] not in extensions:
                extensions.append(file[1])
            # test print("extensions list is {}".format(extensions))
    for extension in extensions:
        #exception for if directory already exists
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file = filename.split('.')
            shutil.move(filename, file[1]+'/')
main()