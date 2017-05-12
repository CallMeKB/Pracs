
import os


def get_fixed_filename(filename):
    new_name = ""
    new_name = filename[0].upper()
    filename = filename[1:]
    # for i, letter in enumerate(filename):
    for i, letter in enumerate(filename):
        try:
            if letter.islower() and filename[i + 1].isupper():
                new_name += letter + '_'
            elif letter.islower() and filename[i-1] == "_":
                new_name += letter.upper()
            elif letter.isupper() and filename[i+1].isupper():
                new_name += letter + '_'
            elif letter == '(' and filename[i-1] != '_':
                new_name += '_' + letter
            elif letter.islower() and filename[i-1] == '(':
                new_name += letter.upper()
            else:
                new_name += letter
        except IndexError:
            new_name += letter
    return new_name


def main():
    os.chdir('Lyrics')
    # loop through each file in the (original) directory
    for dir_name, subdir_list, file_list in os.walk('.'):
        #print(file_list)
        dir_name = dir_name[2:]
        for file in file_list:
            #print(file)
            new_name = file.replace(" ", "_").replace(".TXT", ".txt")
            #print(new_name)
            os.rename(dir_name + '/' + file, dir_name + '/' + new_name)
            new_name_2 = get_fixed_filename(new_name)
            os.rename(dir_name + '/' + new_name, dir_name + '/' + new_name_2)

main()