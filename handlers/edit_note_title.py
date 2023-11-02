from decorators.input_error import input_error
from models.notes import Notes

@input_error
def edit_note_title(args, notes: Notes):
    old_title, new_title = args
    old_title = old_title.title()
    new_title = new_title.title()
    notes.edit_note_title(old_title, new_title)
    return f"Note '{old_title}' title updated to '{new_title}'."
