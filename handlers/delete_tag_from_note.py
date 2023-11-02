from decorators.input_error import input_error
from models.notes import Notes

@input_error
def delete_tag_from_note(args, notes: Notes):
    title, tag = args
    title = title.title()
    notes.delete_tag_from_note(title, tag)
    return f"Tag '{tag}' removed from note '{title}'."
