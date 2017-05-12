"""
program to unpack files and delete empty directories to reset
"""
import os, shutil

os.chdir('FilesToSort')
for dir_name, subdir_list, file_list in os.walk('.'):
    try:
        for file in file_list:
            shutil.move(dir_name + '/' + file, '.')
    except:
        pass
    if dir_name != '.':
        os.rmdir(dir_name)
