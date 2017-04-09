text = input("Enter the sentence: ")
words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
length = 0
for key in words.keys():
    if len(key) > length:
        length = len(key)
for key, value in sorted(words.items()):
    print("{:{}} : {}".format(key, length, value))
