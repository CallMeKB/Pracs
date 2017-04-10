text = input("Enter the sentence: ")
words = {}
for word in text.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
lengths = (len(word) for word in words)
maxLength = max(lengths)
for key, value in sorted(words.items()):
    print("{:{}} : {}".format(key, maxLength, value))
