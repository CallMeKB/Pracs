"""
CP1404 Prac 09 - From Scratch Exercise version 2 
Program to sort through a directory, allow user to catergorise each file  
then move files to their categories subdirectory
"""
import os, shutil


def main():
    # show current directory
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())
    categories = []
    extension_associations = {}
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file = filename.split('.')
            if file[1] not in extension_associations:
                new_category = input("What category would you like to sort {} files into?".format(file[1]))
                extension_associations[file[1]] = new_category
            if new_category not in categories:
                categories.append(new_category)
    for category in categories:
        try:
            os.mkdir(category)
        except FileExistsError:
            pass
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            file = filename.split('.')
            shutil.move(filename, extension_associations[file[1]] + '/')
main()