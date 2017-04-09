text = input("Enter the sentence: ")
words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for key in words.keys():
    length = 0
    if len(key) > length:
        length = len(key)
print(length)
for key, value in words.items():
    print("{:{}} : {}".format(key, length, value))
