from decorators.input_error import input_error
from models.notes import Notes

@input_error
def edit_note_text(args, notes: Notes):
    title, new_text = args
    title = title.title()
    notes.edit_note_text(title, new_text)
    return f"Note '{title}' text updated."
