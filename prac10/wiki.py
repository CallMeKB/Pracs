import wikipedia

valid = False
while not valid:
    page = input("Enter page title: ")
    if page != '':
        try:
            wiki_page = wikipedia.page(page)
            print("Title: {} \nSummary: {} \nUrl: {}".format(wiki_page.title, wiki_page.summary, wiki_page.url))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
    else:
        valid = True
