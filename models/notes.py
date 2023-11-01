from note import Note

class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text, tags=[]):
        note = Note(title, text, tags)
        self.notes.append(note)

    def edit_note_title(self, old_title, new_title):
        for note in self.notes:
            if note.title == old_title:
                note.edit_title(new_title)
                break

    def edit_note_text(self, title, new_text):
        for note in self.notes:
            if note.title == title:
                note.edit_text(new_text)
                break

    def add_tag_to_note(self, title, tag):
        for note in self.notes:
            if note.title == title:
                note.add_tag(tag)
                break

    def remove_tag_from_note(self, title, tag):
        for note in self.notes:
            if note.title == title:
                note.remove_tag(tag)
                break

    def find_notes_by_title(self, title):
        return [note for note in self.notes if note.title == title]

    def find_notes_by_tags(self, search_tags):
        return [note for note in self.notes if note.match_tags(search_tags)]
