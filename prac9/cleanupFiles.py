"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics/Christmas/temp')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
#os.mkdir('temp')

# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        #print(new_name)

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        #shutil.move(filename, 'temp/' + new_name)
        formatted_name = filename[1:]
        for letter in formatted_name:
            if letter == '_':
                underscore_position = formatted_name.index(letter)
                if not formatted_name[underscore_position+1].isupper():
                    formatted_name = formatted_name[:underscore_position+1] + \
                                     formatted_name[underscore_position+1].upper() + \
                                     formatted_name[underscore_position+2]
            elif letter.isupper() or letter == "(":
                capital_position = formatted_name.index(letter)
                if formatted_name[capital_position-1] != '_' and formatted_name[capital_position-1] != '(':
                    formatted_name = formatted_name[:capital_position] + '_' + formatted_name[capital_position:]
        formatted_name = filename[0] + formatted_name
        print(formatted_name)


# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)


