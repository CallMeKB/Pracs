name = 'KeeGanBenTleKy'
sliced_name = name[1:]
print("slicedname{}".format(sliced_name))
for letter in sliced_name:
    if letter.isupper():
        index = sliced_name.index(letter)
        sliced_name = sliced_name[:index] + '_' + sliced_name[index:]
newname = name[0] + sliced_name
print(newname)