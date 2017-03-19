name = input("Enter your name: ")
name_file = open("name.txt", mode='w')
print(name, file=name_file)
name_file.close()

