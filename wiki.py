import wikipediaapi

class WikipediaHelper:
    def __init__(self):
        self.wiki_wiki = wikipediaapi.Wikipedia('en')

    def get_summary(self, query):
        print(f"Searching for: {query}")  # Debug statement
        page = self.wiki_wiki.page(query)
        if page.exists():
            print(f"Found page: {page.title}")  # Debug statement
            return page.summary[0:1000]  # Return a part of the summary
        else:
            print("Page does not exist")  # Debug statement
            return "Jag kunde tyvärr inte hitta någon information om det på Wikipedia."

