import pickle
from models.note import Note


class Notes:
    data_file_name = './data/note.bin'

    def __init__(self):
        try:
            with open(Notes.data_file_name, 'rb') as fn:
                data = pickle.load(fn)
                self.notes = data
        except FileNotFoundError:
            self.notes = []

    def __str__(self):
        title = f'|{"Title":^20}|{"Text":^40}|{"Tags":^30}|\n'
        title += f'|{"-"*20:^20}|{"-"*40:^40}|{"-"*30:^30}|\n'
        for i in self.notes:
            tags = str(i.tags).strip("[]")[:30]
            title += f'|{i.title[:20]:<20}|{i.text[:40]:<40}|{tags:<30}|\n'
        return title

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

    def delete_tag_from_note(self, title, tag):
        for note in self.notes:
            if note.title == title:
                note.remove_tag(tag)
                break

    def find_notes_by_title(self, title):
        return [note for note in self.notes if note.title == title]

    def find_notes_by_tags(self, search_tags):
        return [note for note in self.notes if note.match_tags(search_tags)]

    def sort_notes_by_tag(self, tag):
        sorted_notes = [note for note in self.notes if tag in note.tags]
        sorted_notes.sort(key=lambda x: x.title)
        return sorted_notes

    def delete_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True
        return False

    def save(self):
        with open(Notes.data_file_name, 'wb') as fn:
            pickle.dump(self.notes, fn)
