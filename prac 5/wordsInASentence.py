text = input("Enter the sentence: ")
words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
for key, value in words.items():
    print("{:{}} : {}".format(key, 6, value))
