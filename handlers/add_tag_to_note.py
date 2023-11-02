from decorators.input_error import input_error
from models.notes import Notes

@input_error
def add_tag_to_note(args, notes: Notes):
    '''Whating for title and tag'''
    title, tag = args
    title = title.title()
    notes.add_tag_to_note(title, tag)
    return f"Tag '{tag}' added to note '{title}'."
