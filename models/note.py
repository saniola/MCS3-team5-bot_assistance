class Note:
    def __init__(self, title, text, tags=[]):
        self.title = title
        self.text = text
        self.tags = tags

    def edit_title(self, new_title):
        self.title = new_title

    def edit_text(self, new_text):
        self.text = new_text

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def __str__(self):
        return f"Title: {self.title}\nText: {self.text}\nTags: {', '.join(self.tags)}"

    def match_tags(self, search_tags):
        return all(tag in self.tags for tag in search_tags)
